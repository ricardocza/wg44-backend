from django.urls import path
from . import views

urlpatterns = [path("database/<ticker>/", views.StocksView.as_view())]
