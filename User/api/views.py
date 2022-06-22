from django.shortcuts import render

# Create your views here.
from .serializers import PostSerializer

class PostView(GenericAPIView):
  serializer_class = PostSerializer

  def get(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    post = serializer.save()
    return JsonResponse(PostSerializer(post).data)


