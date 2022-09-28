from rest_framework import routers, urlpatterns
from rest_framework.urls import path

from fingerprints.api.views import FingerprintViewSet, verify_fingerprint

router = routers.DefaultRouter()

router.register("fingerprints", FingerprintViewSet)


app_name = "fingerprints"
urlpatterns = [path("fingerprints/verify/", verify_fingerprint)]

urlpatterns += router.urls
