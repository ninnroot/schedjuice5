import random

from locust import HttpUser, between, task


class UserAction(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def view_student(self):
        student_id = random.randint(1, 10)
        self.client.get(f"/api/v2/students/?obj_id={student_id}", name="/students/:id")

    @task(1)
    def view_guardian(self):
        guardian_id = random.randint(1, 10)
        self.client.get(
            f"/api/v2/guardians/?obj_id={guardian_id}", name="/guardians/:id"
        )

    @task(1)
    def view_staff(self):
        staff_id = random.randint(1, 10)
        self.client.get(f"/api/v2/staffs/?obj_id={staff_id}", name="/staffs/:id")
