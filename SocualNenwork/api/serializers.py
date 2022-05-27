from rest_framework import serializers
from .models import User, Favorite

class CommonSubscribed(metaclass=serializers.SerializerMetaclass):

    is_Favorite = serializers.SerializerMethodField()

    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if request.user.is_anonymous:
            return False
        if Favorite.objects.filter(
                user=request.user, favorites__id=obj.id).exists():
            return True
        else:
            return False


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer, CommonSubscribed):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'is_favorite')


class FavoriteSerializer(serializers.ModelSerializer, CommonSubscribed):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = '__all__'
