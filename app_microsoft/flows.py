from rest_framework.exceptions import ValidationError

from app_microsoft.graph_wrapper.group import MSGroup
from app_microsoft.graph_wrapper.user import MSUser


class CreateAccountFlow:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.ms_user = MSUser()

    def start(self):
        """
        This piece of code is fking stupid. But, that is the only way Microsoft Graph allows.
        Later, this can be carried out by a queue of some sort so that the client doesn't have to wait.
        """
        # this will return a user_id uuid
        res = self.ms_user.create(self.email.split("@")[0], self.email, self.password)

        if res.status_code not in range(199, 300):
            # since the creation fails, abort the entire flow
            raise ValidationError({"MS_ERROR": res.json()})

        # enable mail functionality for the user
        user_id = res.json()["id"]
        res = self.ms_user.enable_mail(user_id, self.email)

        if res.status_code not in range(199, 300):
            # mail-enabling fails.
            # Abort entire flow AND delete the previously created user to maintain data consistency.
            self.ms_user.delete(user_id)
            raise ValidationError({"MS_ERROR": res.json()})

        # so that this can be saved in the local db.
        return user_id


class CreateUserFlow:
    def __init__(self, ms_id: str, user_type: str, new_name: str):
        self.ms_id = ms_id
        if user_type not in {"staff", "student"}:
            raise ValueError("'user_type' can either be 'staff' or 'student'.")
        self.user_type = user_type
        self.new_name = new_name
        self.ms_user = MSUser()

    def start(self):
        res = self.ms_user.assign_license(self.ms_id, self.user_type)

        if res.status_code not in range(199, 300):
            raise ValidationError(
                {"MS_ERROR": res.json(), "step": "license assignment"}
            )

        res = self.ms_user.update_name(self.ms_id, self.new_name)
        if res.status_code not in range(199, 300):
            raise ValidationError({"MS_ERROR": res.json(), "step": "name update"})


class CreateTeamFlow:
    def __init__(self, name: str):
        self.name = name
        self.ms_group = MSGroup()

    def start(self):
        res = self.ms_group.create(self.name)
        if res.status_code not in range(199, 300):
            raise ValidationError({"MS_ERROR": res.json(), "step": "creating group"})

        # after successful creation, we need to get the group_id uuid from the response's headers.
        # why tf is it in the headers? No idea. It's how the Graph API works.
        group_id = res.headers["Content-Location"].split("'")[1::2][0]

        res = self.ms_group.add_channel(group_id, "Announcements")
        if res.status_code not in range(199, 300):
            # if this fails, to maintain data consistency, need to delete previously created group
            self.ms_group.delete(group_id)
            raise ValidationError({"MS_ERROR": res.json(), "step": "creating channel"})
        channel_id = res.json()["id"]

        return {"group_id": group_id, "channel_id": channel_id}
