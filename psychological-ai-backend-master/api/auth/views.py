from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


# Managing Users


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# User In's/Out's

@api_view(['POST'])
def user_register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        res = {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }

        return Response(res, status=201)
