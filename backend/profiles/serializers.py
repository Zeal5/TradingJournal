from rest_framework import serializers
from .models import Profile


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Profile
        fields = [
            "username",
            "email",
            "password",
            "password2",
            "tc",
            "status",
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password do not match"
            )

        return attrs

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)



class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = Profile
        fields = [
            "email",
            "password",
        ]
    
