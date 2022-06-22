from django.contrib import admin
from django.urls import path
from .views import views

urlpatterns = [
    path('api', views.PostView.as_view(),'api'),
]
