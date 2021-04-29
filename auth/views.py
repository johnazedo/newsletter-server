from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.models import InviteCode
from auth.serializers import RegisterSerializer, InviteCodeSerializer, CheckEmailExistsSerializer


class RegisterView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class CheckInviteCodeView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = InviteCodeSerializer
    lookup_field = 'code'
    queryset = InviteCode.objects.all()


class CheckEmailExistsView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CheckEmailExistsSerializer

    def get(self, request, *args, **kwargs):
        email = request.query_params.get('email', None)
        used = User.objects.filter(email=email).exists()
        serializer = self.serializer_class(instance={'used':used})
        return JsonResponse(serializer.data)


