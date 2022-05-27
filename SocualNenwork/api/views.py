from http import HTTPStatus
from rest_framework import viewsets
from .models import User, Post, Favorite
from .serializers import UserSerializer, PostSerializer, FavoriteSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteViewSet(viewsets.ModelViewSet):

    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    model = Favorite

    def create(self, request, *args, **kwargs):
        post_id = int(self.kwargs['post_id'])
        post = get_object_or_404(Post, id=post_id)
        self.model.objects.create(
            user=request.user, post=post)
        return Response(HTTPStatus.CREATED)

    def delete(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']
        user_id = request.user.id
        object = get_object_or_404(
            self.model, user__id=user_id, post__id=post_id)
        object.delete()
        return Response(HTTPStatus.NO_CONTENT)

