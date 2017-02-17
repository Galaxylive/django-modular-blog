from django import forms
from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    """
    Base admin capable of displaying specified text fields as char fields
    """
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(BaseAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)

        display_as_charfield = getattr(self, 'display_as_charfield', [])
        display_as_choicefield = getattr(self, 'display_as_choicefield', [])

        if db_field.name in display_as_charfield:
            formfield.widget = forms.TextInput(attrs=formfield.widget.attrs)
        elif db_field.name in display_as_choicefield:
            formfield.widget = forms.Select(choices=formfield.choices,
                                            attrs=formfield.widget.attrs)

        return formfield
