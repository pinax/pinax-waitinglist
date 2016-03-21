from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r"^list_signup/$", views.ListSignupView.as_view(), name="list_signup"),
    url(r"^ajax_list_signup/$", views.ajax_list_signup, name="ajax_list_signup"),
    url(r"^survey/thanks/$", TemplateView.as_view(template_name="pinax/waitinglist/thanks.html"),
        name="survey_thanks"),
    url(r"^survey/(?P<code>.*)/$", views.SurveyView.as_view(), name="survey"),
    url(r"^success/$", TemplateView.as_view(template_name="pinax/waitinglist/success.html"),
        name="success"),
]
