from django.urls import path

from . import views

urlpatterns = [
    path("visits/", views.VisitsView.as_view())
]