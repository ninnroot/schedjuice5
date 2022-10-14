from django.db.models import F, TextField
from django.db.models.functions import Concat
from django.db.models.lookups import Value
from django_cte import CTEManager, With

from schedjuice5.managers import CustomManager


class GroupManager(CTEManager, CustomManager):
    def get_nested(self):
        def idk(cte):
            return With(
                self.filter(parent_id__isnull=True)
                .values("name", path=F("name"))
                .all()
                .union(
                    cte.join(self.model, parent_id=cte.col.parent_id).values(
                        "name",
                        path=Concat(
                            cte.col.path,
                            Value("/"),
                            F("name"),
                            output_field=TextField(),
                        ),
                    ),
                    all=True,
                )
            )

        cte = With.recursive(idk)
        results = (
            cte.join(self.model, name=cte.col.name)
            .with_cte(cte)
            .annotate(path=cte.col.path)
            .order_by("path")
        )
        return results
