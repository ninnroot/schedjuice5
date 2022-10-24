from django.db.models import F, IntegerField, Prefetch, TextField
from django.db.models.functions import Cast, Concat
from django.db.models.lookups import Value
from django_cte import CTEManager, With

from schedjuice5.managers import CustomManager


class GroupManager(CTEManager, CustomManager):
    def get_nested(self, root_id=None):
        x = {}
        if root_id:
            x = {"pk": root_id}

        def idk(cte):
            return (
                self.model.objects.filter(parent__isnull=True, **x)
                .values(
                    "id",
                    "parent_id",
                    "parent",
                    "name",
                    path=Cast(F("name"), output_field=TextField()),
                    depth=Value(0, output_field=IntegerField()),
                )
                .union(
                    cte.join(self.model, parent_id=cte.col.id).values(
                        "id",
                        "parent_id",
                        "parent",
                        "name",
                        path=Concat(
                            cte.col.path,
                            Value("/"),
                            (F("name")),
                            output_field=TextField(),
                        ),
                        depth=cte.col.depth + Value(1, output_field=IntegerField()),
                    ),
                    all=True,
                )
            )

        cte = With.recursive(idk)
        results = (
            cte.join(self.model, name=cte.col.name)
            .with_cte(cte)
            .annotate(path=cte.col.path, depth=cte.col.depth)
        )

        highest_depth = results.order_by("-depth").first().depth
        related_str = "parent"
        if highest_depth > 0:
            for i in range(highest_depth):
                related_str = related_str + "__parent"

        return results.select_related(related_str)
