from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializers, UserSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset= get_user_model().objects.all()
    serializer_class = UserSerializer
