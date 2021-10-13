from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('register/',register.as_view(),name='register'),




]