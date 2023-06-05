from rest_framework import serializers
from .models import Visits

class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields=["id", "ip", "created_at"]
        read_only_fields = ["ip", "created_at"]

    def create(self, validated_data):
        validated_data["ip"] = self.context.get("request").META.get("REMOTE_ADDR")
        return Visits.objects.create(**validated_data)