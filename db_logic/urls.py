from django.urls import path
from . import views

urlpatterns = [
    path("database/<ticker>/", views.StocksView.as_view()),
    path("database/<ticker>/list/", views.ListView.as_view()),
    path("database/clear/<ticker>/", views.StocksDestroyView.as_view()),
]
