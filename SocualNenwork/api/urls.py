from django.urls import include, path
from .views import UserViewSet, PostViewSet, FavoriteViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()


router.register('users', UserViewSet, basename='users')
router.register(r'posts', PostViewSet, basename='posts')


urlpatterns = [
    path('posts/<post_id>/favorite/',
         FavoriteViewSet.as_view({'post': 'create',
                                  'delete': 'delete'}), name='favorite'),
    path('', include(router.urls)),
]
