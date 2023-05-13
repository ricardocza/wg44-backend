from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 50

    def paginate_queryset(self, queryset, request, view=None):
        queryset = queryset.order_by("-id")
        return super().paginate_queryset(queryset, request, view)
