from django.contrib import admin
from django.urls import path
from .views import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api', views.PostView.as_view(),'api'),
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)