import importlib

from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.waitinglist"
    label = "pinax_waitinglist"
    verbose_name = _("Pinax Waiting List")

    def ready(self):
        importlib.import_module("pinax.waitinglist.receivers")
