from django.conf.urls import include, url


urlpatterns = [
    url(r"^", include("pinax.waitinglist.urls", namespace="pinax_waitinglist")),
]
