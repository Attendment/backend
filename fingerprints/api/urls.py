from rest_framework import routers, urlpatterns

from fingerprints.api.views import FingerprintViewSet

router = routers.DefaultRouter()

router.register("fingerprints", FingerprintViewSet)

app_name = "fingerprints"
urlpatterns = []

urlpatterns += router.urls
