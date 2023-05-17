from django.urls import path
from . import views

urlpatterns = [
    path("database/<ticker>", views.StocksView.as_view()),
    path("database/<ticker>/list/", views.ListView.as_view()),
    path("database/<ticker>/list/mean/", views.ListAveragesView.as_view()),
    path("database/list/current-close/", views.LastCloseView.as_view()),
    path("database/clear/", views.StocksDestroyView.as_view()),
]
