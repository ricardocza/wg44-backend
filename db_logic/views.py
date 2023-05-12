from django.shortcuts import render
from rest_framework import generics
from .serializers import StocksSerializer
from .models import Stocks


# Create your views here.
class StocksView(generics.ListCreateAPIView):
    model = Stocks
    serializer_class = StocksSerializer
    queryset = Stocks.objects.all()
    lookup_field = "ticker"

    def perform_create(self, serializer):
        count = Stocks.objects.count()
        current_close = serializer.validated_data["closed_price"]
        if count < 6:
            current_stocks = Stocks.objects.order_by("-id")
            for i, row in enumerate(current_stocks):
                if i == 0:
                    row.diff_1 = current_close - row.pred_1
                    row.error_1 = row.diff_1 / current_close
                elif i == 1:
                    row.diff_2 = current_close - row.pred_2
                    row.error_2 = row.diff_2 / current_close
                elif i == 2:
                    row.diff_3 = current_close - row.pred_3
                    row.error_3 = row.diff_3 / current_close
                elif i == 3:
                    row.diff_4 = current_close - row.pred_4
                    row.error_4 = row.diff_4 / current_close
                elif i == 4:
                    row.diff_5 = current_close - row.pred_5
                    row.error_5 = row.diff_5 / current_close

                row.save()

        else:
            current_stocks = Stocks.objects.order_by("-id")[:6]
            for i, row in enumerate(current_stocks):
                if i == 0:
                    row.diff_1 = current_close - row.pred_1
                    row.error_1 = row.diff_1 / current_close
                elif i == 1:
                    row.diff_2 = current_close - row.pred_2
                    row.error_2 = row.diff_2 / current_close
                elif i == 2:
                    row.diff_3 = current_close - row.pred_3
                    row.error_3 = row.diff_3 / current_close
                elif i == 3:
                    row.diff_4 = current_close - row.pred_4
                    row.error_4 = row.diff_4 / current_close
                elif i == 4:
                    row.diff_5 = current_close - row.pred_5
                    row.error_5 = row.diff_5 / current_close
                elif i == 5:
                    row.diff_6 = current_close - row.pred_6
                    row.error_6 = row.diff_6 / current_close

                row.save()

        return serializer.save(ticker=self.kwargs["ticker"])
