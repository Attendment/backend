from rest_framework import serializers

from fingerprints.models import Fingerprint


class FingerprintReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fingerprint
        fields = ["id", "created", "file", "binary"]


class FingerprintWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fingerprint
        fields = ["id", "created", "file", "binary"]


class FingerprintSerializerMinimal(serializers.ModelSerializer):
    class Meta:
        model = Fingerprint
        fields = ["id", "file", "binary"]
