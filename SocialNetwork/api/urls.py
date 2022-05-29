from django.urls import include, path
from .views import (UserViewSet, PostViewSet, FavoriteListViewSet,
                    FavoriteViewSet, RecieveToken)
from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()


router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')


urlpatterns = [
    path('posts/<post_id>/favorite/',
         FavoriteViewSet.as_view({'post': 'create',
                                  'delete': 'delete'}), name='favorite'),
    path('posts/favorite/',
         FavoriteListViewSet.as_view({'get': 'list'}), name='favorite_list)'),
    path('auth/', RecieveToken.as_view()),
    path('', include(router.urls)),
]
