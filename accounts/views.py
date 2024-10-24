from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, UserSerializer, UserProfileSerializer, UserProfilePointSerializer, UsersProfilesSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Profile

from django.contrib.auth import get_user_model
User = get_user_model()


class UserRegister(APIView):

    serializer_class = UserRegisterSerializer

    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)

        if ser_data.is_valid():
            User.objects.create_user(
                email=ser_data.validated_data['email'],
                phone_number=ser_data.validated_data['phone_number'],
                full_name=ser_data.validated_data['full_name'],
                study_field=ser_data.validated_data['full_name'],
                student_id=ser_data.validated_data['full_name'],
                password=ser_data.validated_data['password'],
            )
            Profile.objects.create(
                user = User.objects.get(phone_number=ser_data.validated_data['phone_number'])
            )
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApi(APIView):

    serializer_class = UserProfileSerializer

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        ser_data = UserProfileSerializer(data=profile)
        return Response(ser_data, status.HTTP_200_OK)


class AddScoreView(APIView):

    serializer_class = UserProfilePointSerializer

    def post(self, request):
        ser_data = UserProfilePointSerializer(data=request.POST)
        profile = Profile.objects.get(user=request.user)
        point = profile.point
        if ser_data.is_valid():
            new_point = ser_data.validated_data["point"] + point
        Profile.objects.filter(pk=profile.pk).update(point=new_point)
        return Response(ser_data.data, status.HTTP_200_OK)


class AllProfilesView(APIView):
    serializer_class = UsersProfilesSerializer

    def get(self, request):
        profiles = Profile.objects.all()
        ser_data = UsersProfilesSerializer(instance=profiles, many=True)

        return Response(ser_data.data, status.HTTP_200_OK)