from rest_framework.serializers import ModelSerializer
from users.models import User
from .models import ImageModel


class ImageSerializer(ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = {'id', 'email', 'username'}

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['username'], validated_data['password'])
        return user

