from django.forms.renderers import TemplatesSetting


class CustomFormRenderer(TemplatesSetting):
    """This defines the default template to use for __all__ forms
    in the project. (Referenced by FORM_RENDERER in settings.py)."""

    form_template_name = "_form_template.html"
