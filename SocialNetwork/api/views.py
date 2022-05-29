from http import HTTPStatus

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from .models import Favorite, Post, User
from .serializers import (FavoriteListSerializer, FavoriteSerializer,
                          PostCreateSerializer, PostSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    Set viewset for User model.
    """
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    """
    Set viewset for Post model.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        else:
            return PostSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    Set viewset for Favorite model.
    """
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    model = Favorite

    def create(self, request, *args, **kwargs):
        post_id = int(self.kwargs.get('post_id'))
        post = get_object_or_404(Post, id=post_id)
        if post.author == request.user:
            response = {'response': 'You do not add in favorite your posts!'}
            return Response(response, HTTPStatus.NO_CONTENT)
        if self.model.objects.filter(user=request.user, post=post).exists():
            response = {'response': 'object is exists!'}
            return Response(response, HTTPStatus.NO_CONTENT)
        serialozers = PostCreateSerializer(post)
        self.model.objects.create(
            user=request.user, post=post)
        return Response(serialozers.data, HTTPStatus.CREATED)

    def delete(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_id')
        user_id = request.user.id
        object = get_object_or_404(
            self.model, user__id=user_id, post__id=post_id)
        object.delete()
        response = {'response': 'object was deleted!'}
        return Response(response, HTTPStatus.NO_CONTENT)


class FavoriteListViewSet(viewsets.ModelViewSet):
    """
    Set viewset for Favorite model.
    """
    serializer_class = FavoriteListSerializer
    queryset = Favorite.objects.all()
    model = Favorite

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


def get_token(user):
    """
    Create jwt token for login is app.
    """
    access = AccessToken.for_user(user)
    return {'access': str(access)}


class RecieveToken(APIView):
    """
    Recieve jwt token for login is app.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
        except KeyError:
            return Response(HTTPStatus.NOT_FOUND)
        user = get_object_or_404(User, username=username, password=password)
        response = {'auth_token': get_token(user)}
        return Response(response, HTTPStatus.OK)
