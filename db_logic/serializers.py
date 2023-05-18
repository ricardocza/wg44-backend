from rest_framework import serializers
from .models import Stocks


class TimeField(serializers.DateTimeField):
    def to_representation(self, value):
        return value.strftime("%H:%M:%S")


class RoundToFiveField(serializers.IntegerField):
    def to_representation(self, value):
        current_ticker = self.context["request"].parser_context["kwargs"]["ticker"]
        if current_ticker == "WINFUT":
            return round(value / 5) * 5
        elif current_ticker == "WDOFUT":
            return round(value / 0.5) * 0.5
        else:
            return round(value / 0.01) * 0.01


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
            "diff_1",
            "diff_2",
            "diff_3",
            "diff_4",
            "diff_5",
            "diff_6",
            "error_1",
            "error_2",
            "error_3",
            "error_4",
            "error_5",
            "error_6",
            "created_at",
        ]

        read_only_fields = ["created_at", "ticker"]

    def create(self, validated_data):
        return Stocks.objects.create(**validated_data)


class ListSerializer(serializers.ModelSerializer):
    created_at = TimeField()
    closed_price = RoundToFiveField()
    pred_1 = RoundToFiveField()
    pred_2 = RoundToFiveField()
    pred_3 = RoundToFiveField()
    pred_4 = RoundToFiveField()
    pred_5 = RoundToFiveField()
    pred_6 = RoundToFiveField()

    class Meta:
        model = Stocks
        fields = "__all__"

        read_only_fields = ["created_at", "ticker"]
