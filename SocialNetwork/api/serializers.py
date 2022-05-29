from rest_framework import serializers

from .models import Favorite, Post, User


class IsFavorite(metaclass=serializers.SerializerMetaclass):
    """
    Set favorite status for main serializer.
    """
    is_favorite = serializers.SerializerMethodField()

    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if request.user.is_anonymous:
            return False
        if Favorite.objects.filter(
                user=request.user, post=obj).exists():
            return True
        else:
            return False


class UserSerializer(serializers.ModelSerializer):
    """
    Set serializer for User model.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }


class PostCreateSerializer(serializers.ModelSerializer):
    """
    Set serializer for create objects of Post model.
    """
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer, IsFavorite):
    """
    Set serializer for get objects of Post model.
    """
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'is_favorite')


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Set serializer for Favorite model.
    """
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = '__all__'


class FavoriteListSerializer(serializers.ModelSerializer):
    """
    Set serializer for Favorite model.
    """
    post = PostSerializer()

    class Meta:
        model = Favorite
        exclude = ('id', 'user')
