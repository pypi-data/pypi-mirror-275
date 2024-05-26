# paper-admin-permission-field

Permission field implementation tailored for paper-admin.

[![PyPI](https://img.shields.io/pypi/v/paper-admin-permission-field.svg)](https://pypi.org/project/paper-admin-permission-field/)
[![Software license](https://img.shields.io/pypi/l/paper-admin-permission-field.svg)](https://pypi.org/project/paper-admin-permission-field/)

## Compatibility

-   `python` >= 3.7
-   `django` >= 3.2
-   `paper-admin` >= `7.7.0`

## Installation

Install the latest release with pip:

```shell
pip install paper-admin-permission-field
```

## Usage

```python
# custom_users/admin.py

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group, Permission, User

from paper_permission_field.forms import PermissionsField


class GroupAdminForm(forms.ModelForm):
    permissions = PermissionsField(
        required=False,
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = forms.ALL_FIELDS


class CustomUserChangeForm(UserChangeForm):
    user_permissions = PermissionsField(
        required=False,
        queryset=Permission.objects.all()
    )


class CustomGroupAdmin(GroupAdmin):
    form = GroupAdminForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)
```

Result:

![image](https://github.com/dldevinc/paper-admin-permission-field/assets/6928240/43fb89df-ef4f-4791-b22f-484baec83cf5)
