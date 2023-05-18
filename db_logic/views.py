from django.shortcuts import render
from django.db.models import Avg, Count
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StocksSerializer, ListSerializer
from .models import Stocks
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import PostPermission
from .pagination import CustomPagination
from django.forms.models import model_to_dict


# Create your views here.
class StocksView(generics.CreateAPIView):
    model = Stocks
    serializer_class = StocksSerializer
    queryset = Stocks.objects.all()
    pagination_class = CustomPagination
    lookup_field = "ticker"
    authentication_classes = [JWTAuthentication]
    permission_classes = [PostPermission]

    def perform_create(self, serializer):
        count = Stocks.objects.count()
        current_close = serializer.validated_data["closed_price"]
        if count < 6:
            current_stocks = Stocks.objects.filter(
                ticker=self.kwargs["ticker"]
            ).order_by("-id")
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
            current_stocks = Stocks.objects.filter(
                ticker=self.kwargs["ticker"]
            ).order_by("-id")[:6]
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


class ListView(generics.ListAPIView):
    model = Stocks
    serializer_class = ListSerializer
    queryset = Stocks.objects.all()
    pagination_class = CustomPagination
    lookup_field = "ticker"

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(ticker=self.kwargs["ticker"])
        return self.list(request, *args, **kwargs)


class ListAveragesView(APIView):
    model = Stocks
    lookup_field = "ticker"
    queryset = Stocks.objects.exclude(
        diff_6__isnull=True,
    )

    def get(self, request, *args, **kwargs):
        queryset_filter = self.queryset.filter(ticker=kwargs["ticker"])

        mean_values = queryset_filter.aggregate(
            mean_diff_1=Avg("diff_1"),
            mean_diff_2=Avg("diff_2"),
            mean_diff_3=Avg("diff_3"),
            mean_diff_4=Avg("diff_4"),
            mean_diff_5=Avg("diff_5"),
            mean_diff_6=Avg("diff_6"),
        )

        return Response(mean_values)


class StocksDestroyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PostPermission]

    def delete(self, request):
        last_row = Stocks.objects.order_by("id").last()
        last_row.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LastCloseView(generics.ListAPIView):
    model = Stocks
    serializer_class = ListSerializer
    queryset = Stocks.objects.all()

    def get(self, request, *args, **kwargs):
        asset_list = []
        prices = []
        id = []
        queryset = Stocks.objects.values_list("id", "ticker", "closed_price")
        for i in range(len(queryset) - 1, -1, -1):
            if queryset[i][1] not in asset_list:
                id.append(queryset[i][0])
                asset_list.append(queryset[i][1])
                prices.append(queryset[i][2])

        response = []
        for i in range(len(asset_list)):
            response.append(
                {"id": id[i], "asset": asset_list[i], "last_price": prices[i]}
            )
        return Response(response)
