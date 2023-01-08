from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken


# create JWT token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, formate=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response(
                {"message": "Registration Successful", "token": token},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, formate=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response(
                    {"message": "Login Sucessful", "token": token},
                    status=status.HTTP_200_OK,
                )

            return Response(
                {"message": "Invalid Email or Password"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
