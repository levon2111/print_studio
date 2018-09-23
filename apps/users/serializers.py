from rest_framework import serializers

from apps.core.utils import generate_unique_key, send_email_job_registration
from apps.users.models import User
from apps.users.validators import check_valid_password


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    repeat_password = serializers.CharField()
    name = serializers.CharField(
        required=False,
        allow_blank=True,
    )
    phone_number = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=255,
    )

    @staticmethod
    def save_user(validated_data):
        user = User(email=validated_data['email'], name=validated_data['name'],
                    phone_number=validated_data['phone_number'])
        user.set_password(validated_data['password'])
        user.is_active = False
        user.email_confirmation_token = generate_unique_key(user.email)
        user.save()

        send_email_job_registration(
            'Print Studio',
            user.email,
            'account_confirmation',
            {
                'token': user.email_confirmation_token,
                'name': user.name
            },
            'Welcome to Print Studio',
        )

    def validate(self, data):
        check_valid_password(data)
        self.check_valid_email(data['email'])

        return data

    @staticmethod
    def check_valid_email(value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError({'email': ['This email address has already exist.']})

        return value
