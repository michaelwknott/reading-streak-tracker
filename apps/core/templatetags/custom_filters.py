# apps/core/templatetags/custom_filters.py

from django import template

register = template.Library()


@register.filter(name="tailwind_message_tag")
def tailwind_message_tag(message_tag):
    """
    Used to dynamically set the TailwindCSS class for a message.
    Inside a template, use it like this: {{ message.tags|tailwind_message_tag }}.

    The mapping below will replace the class it encounters, e.g. "debug", with the values
    provided in value string. That way the correct styling is applied dynamically, depending
    on the class of the message.
    """
    classes = {
        "debug": "debug bg-gray-100 border border-gray-500 "
        "text-gray-700 px-4 py-3 rounded relative",
        "info": "info bg-blue-100 border border-blue-500 "
        "text-blue-700 px-4 py-3 rounded relative",
        "success": "success bg-green-100 border border-green-500 "
        "text-green-700 px-4 py-3 rounded relative",
        "warning": "warning bg-yellow-100 border border-yellow-500 "
        "text-yellow-700 px-4 py-3 rounded relative",
        "error": "error bg-red-100 border border-red-500 "
        "text-red-700 px-4 py-3 rounded relative",
    }
    return classes.get(message_tag, "")
