from rest_framework import serializers
from .models import Stocks


class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = [
            "id",
            "ticker",
            "ticker_name",
            "closed_price",
            "pred_1",
            "pred_2",
            "pred_3",
            "pred_4",
            "pred_5",
            "pred_6",
        ]
        read_only_fields = ["created_at", "ticker"]

    def create(self, validated_data):
        return Stocks.objects.create(**validated_data)
