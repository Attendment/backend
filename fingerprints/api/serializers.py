from rest_framework import serializers

from fingerprints.models import Fingerprint, FingerprintVerification


class FingerprintReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fingerprint
        fields = ["id", "created", "fingerprint_id"]


class FingerprintWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fingerprint
        fields = ["id", "created", "fingerprint_id"]


class FingerprintSerializerMinimal(serializers.ModelSerializer):
    class Meta:
        model = Fingerprint
        fields = ["id", "fingerprint_id"]

class FingerprintVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingerprintVerification
        fields = ["id", "created", "state", "student"]
