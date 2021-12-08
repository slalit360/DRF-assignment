from rest_framework import serializers
from account.models import User
from django.contrib.auth import authenticate


class RegisterUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['name'],
                                        validated_data['email'],
                                        validated_data['password'],
                                        )
        return user

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            "name": {"error_messages": {"blank": "name required"}},
            "email": {"error_messages": {"blank": "email required"}},
            "password": {'write_only': True, "error_messages": {"blank": "Password required"}},
        }
        read_only_fields = ('id', 'is_admin')


class UserSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['name'],
                                        validated_data['email'],
                                        validated_data['password'],
                                        )
        return user

    class Meta:
        model = User
        fields = (
            'id', 'name', 'email', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, required=True, error_messages={'required': 'Username required'})
    password = serializers.CharField(max_length=255, required=True, error_messages={"required": "Password required"})

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, attrs, ):
        user = authenticate(
            email=attrs['username'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError('Invalid email or password')
        self.instance = user
        return user
