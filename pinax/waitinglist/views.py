from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView

from .forms import SurveyForm, WaitingListEntryForm
from .models import SurveyInstance, WaitingListEntry
from .signals import signed_up


@require_POST
def ajax_list_signup(request):
    form = WaitingListEntryForm(request.POST)
    if form.is_valid():
        entry = form.save()
        signed_up.send(sender=ajax_list_signup, entry=entry)
        try:
            data = {
                "location": reverse("pinax_waitinglist:survey", args=[entry.surveyinstance.code])
            }
        except SurveyInstance.DoesNotExist:
            data = {
                "html": render_to_string("pinax/waitinglist/_success.html", {
                }, request=request)
            }
    else:
        data = {
            "html": render_to_string("pinax/waitinglist/_list_signup.html", {
                "form": form,
            }, request=request)
        }
    return JsonResponse(data)


class ListSignupView(CreateView):
    """
    Add email address to signup list.
    """
    model = WaitingListEntry
    form_class = WaitingListEntryForm
    template_name = "pinax/waitinglist/list_signup.html"

    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            "referrer": self.request.META.get("HTTP_REFERER", ""),
            "campaign": self.request.GET.get("wlc", "")
        })
        return initial

    def form_valid(self, form):
        self.object = form.save()
        signed_up.send(sender=self, entry=self.object)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        success_url = None

        try:
            success_url = reverse(
                "pinax_waitinglist:survey",
                args=[self.object.surveyinstance.code]
            )
        except SurveyInstance.DoesNotExist:
            pass

        if success_url is None:
            success_url = reverse("pinax_waitinglist:success")
        elif not success_url.startswith("/"):
            success_url = reverse(success_url)
        return success_url


class SurveyView(UpdateView):
    """
    Show a survey form or POST survey answers.
    """
    model = SurveyInstance
    form_class = SurveyForm
    slug_url_kwarg = "code"
    slug_field = "code"
    template_name = "pinax/waitinglist/survey.html"
    success_url = reverse_lazy("pinax_waitinglist:survey_thanks")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"survey": self.object.survey})
        return kwargs

    def form_valid(self, form):
        form.save(self.object)
        return HttpResponseRedirect(self.get_success_url())
