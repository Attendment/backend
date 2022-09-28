from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from fingerprints.api.serializers import (
    FingerprintReadSerializer,
    FingerprintWriteSerializer,
)

from fingerprints.models import Fingerprint


@api_view(["POST"])
def verify_fingerprint(request):
    """
    Get the reqest data which is a fingerprint id, and
    verify if that student associated with that id is
    supposed to be seated in the room for the exams being
    conducted.
    """
    if request.POST == "POST":
        print(request.data)


class FingerprintViewSet(viewsets.ModelViewSet):
    queryset = Fingerprint.objects.all()  # type: ignore

    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "destroy"]:
            return FingerprintReadSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return FingerprintWriteSerializer
