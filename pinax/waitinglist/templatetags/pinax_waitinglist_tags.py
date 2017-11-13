from django import template

from ..forms import WaitingListEntryForm

register = template.Library()


@register.simple_tag(takes_context=True)
def waitinglist_entry_form(context):
    """
    Get a (new) form object to post a new comment.

    Syntax::

        {% waitinglist_entry_form as [varname] %}

    """
    initial = {}
    if "request" in context:
        initial.update({
            "referrer": context["request"].META.get("HTTP_REFERER", ""),
            "campaign": context["request"].GET.get("wlc", "")
        })
    return WaitingListEntryForm(initial=initial)
