from rest_framework import serializers
from .models import Visits

class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields=["id", "ip", "created_at"]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        return Visits.objects.create(**validated_data)