from rest_framework import viewsets
from fingerprints.api.serializers import (
    FingerprintReadSerializer,
    FingerprintWriteSerializer,
)

from fingerprints.models import Fingerprint


class FingerprintViewSet(viewsets.ModelViewSet):
    queryset = Fingerprint.objects.all()  # type: ignore

    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "destroy"]:
            return FingerprintReadSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return FingerprintWriteSerializer
