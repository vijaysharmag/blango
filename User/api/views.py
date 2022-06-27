from django.shortcuts import render
from rest_framework import generics
from blog.api.serializers import PostSerializer
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.authtoken import views
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject


class PostView(GenericAPIView):
  serializer_class = PostSerializer

  def get(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    post = serializer.save()
    return JsonResponse(PostSerializer(post).data)



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


