from itertools import groupby

from django import forms
from django.apps import apps
from paper_admin.admin.widgets import AdminCheckboxTree


class PermissionModelChoiceIterator(forms.models.ModelChoiceIterator):
    def __iter__(self):
        if self.field.empty_label is not None:
            yield "", self.field.empty_label

        queryset = self.queryset

        # Can't use iterator() when queryset uses prefetch_related()
        if not queryset._prefetch_related_lookups:
            queryset = queryset.iterator()

        for key, group in groupby(queryset, key=lambda x: x.content_type.app_label):
            try:
                app_config = apps.get_app_config(key)
            except LookupError:
                label = "{} (Error: application not found!)".format(key)
            else:
                if app_config.verbose_name:
                    label = "{} ({})".format(app_config.verbose_name, app_config.label)
                else:
                    label = app_config.label

            yield label, [
                self.choice(obj)
                for obj in group
            ]


class PermissionsField(forms.ModelMultipleChoiceField):
    widget = AdminCheckboxTree
    iterator = PermissionModelChoiceIterator

    def label_from_instance(self, obj):
        return "%s | %s" % (obj.content_type.name, obj.name)
