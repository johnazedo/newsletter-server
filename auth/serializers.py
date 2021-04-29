from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField, BooleanField
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.validators import UniqueValidator
import uuid

from auth.models import InviteCode

class CheckEmailExistsSerializer(Serializer):
    used = serializers.BooleanField()


class InviteCodeSerializer(ModelSerializer):
    class Meta:
        model = InviteCode
        fields = ['code']


class RegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = CharField(write_only=True, required=True, validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'password', 'password2')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
        )

        InviteCode.objects.create(
            code = uuid.uuid4().hex[:8].upper(),
            user = user
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
