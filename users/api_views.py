import datetime
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from project import settings
from .models import Role, User
from .serializers import (
    LoginSerializer,
    ResetPasswordConfirmSerializer,  
    UserSerializer,
    ForgotPasswordSerializer
)
from rest_framework_simplejwt.tokens import RefreshToken
from .security import create_token, decrypt_token
import random

content_type = "application/json;charset=UTF-8"




@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user :User= authenticate(request=request, email=email, password=password)
        if user is not None:
            if (user.has_role(Role.STUDENT)or user.has_role(Role.GUARDIAN) or user.has_role(Role.TEACHER)) and not user.has_reset_password :
                return Response(data={"error": "يجب تغيير كلمة المرور قبل تسجيل الدخول"}, 
                                status=status.HTTP_400_BAD_REQUEST, content_type=content_type)
                
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response(data={
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
                "user": user_serializer.data
            }, 
            status=status.HTTP_201_CREATED)
            
        return Response(data={"error": "كلمة المرور او البريد الالكتروني غير صحيح"},
                    status=status.HTTP_400_BAD_REQUEST, content_type=content_type)
    print("errors", serializer.errors)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ForgetPasswordView(GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = get_object_or_404(User, email=email)
        otp = str(random.randint(100000, 999999))
        print(otp)
        payload = {
            'user_id': user.id,
            'email': user.email,
            'otp': otp,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=10)
        }
        token = create_token(payload)

        send_mail(
            'OTP for Forget Password',
            f'Your Otp is {otp}',
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        return Response({
            'token': token
        }, status=200)


class ResetPasswordConfirmView(GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer

    def post(self, request, *args, **kwargs):
        print("*"*100)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = serializer.validated_data['otp']
        enc_token = serializer.validated_data['token']
        data = decrypt_token(enc_token)
        if data['status']:
            otp_real = data['payload']['otp']
            if otp == otp_real:
                email = data['payload']['email']
                user = User.objects.get(email=email)
                new_password = serializer.validated_data.get('new_password', None)
                if new_password:
                    user.set_password(new_password)
                    user.has_reset_password = True
                    user.save()
                refresh_token = RefreshToken.for_user(user)
                return Response({
                    'access_token': str(refresh_token.access_token),
                    "user": UserSerializer(user).data,
                    "refresh_token": str(refresh_token)
                }, status=status.HTTP_200_OK, content_type=content_type)
            else:
                return Response({
                    'message': 'رمز التحقق غير صحيح'
                }, status=status.HTTP_400_BAD_REQUEST, content_type=content_type)
        else:
            return Response({
                'message': 'انتهت صلاحية رمز التحقق... حاول مرة أخرى',
            }, status=status.HTTP_400_BAD_REQUEST, content_type=content_type)
            
            

class CustomIsAuthenticated(IsAuthenticated):
    message = 'قم بتسجيل الدخول اولاً'
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            raise AuthenticationFailed(self.message)
        return True            
            
@api_view(['POST'])
@permission_classes([CustomIsAuthenticated])
def me(request):
    serializer = UserSerializer(request.user)
    refresh = RefreshToken.for_user(request.user)
    return Response(data={
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh),
        "user": serializer.data
    }, status=status.HTTP_200_OK)

