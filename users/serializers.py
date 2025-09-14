from rest_framework import serializers

from users.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_password(self, value: str) -> str:
        return make_password(value)
