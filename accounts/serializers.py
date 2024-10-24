from rest_framework import serializers
from .models import User, Profile


def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin cant in email')


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name','study_field','student_id' , 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'validators': (clean_email,)},
        }

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username cant be admin')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password must match')
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserProfilePointSerializer(serializers.Serializer):
    point =  serializers.IntegerField()

class UsersProfilesSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"

    def get_user(self, obj):
        user = User.objects.get(email=obj.user)
        return UserSerializer(instance=user).data


