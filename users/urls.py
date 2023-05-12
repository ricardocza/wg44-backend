from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("user/", views.UserView.as_view()),
    path("user/login/", jwt_views.TokenObtainPairView.as_view()),
]
