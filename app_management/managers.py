from django.db.models import F, TextField
from django.db.models.functions import Concat
from django.db.models.lookups import Value
from django_cte import CTEManager, With

from schedjuice5.managers import CustomManager


class GroupManager(CTEManager, CustomManager):
    def get_nested(self):
        def idk(cte):
            return With(
                self.filter(parent__isnull=True)
                .all()
                .union(cte.join(self.model, parent=cte.col.parent))
            )

        cte = With.recursive(idk)
        results = cte.join(self.model, name=cte.col.name).with_cte(cte)
        return results
