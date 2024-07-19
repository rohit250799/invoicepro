from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import UserProfileInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileInfo
        fields = ('id', 'username', 'email', 'password', 'plan_type', 'user_country', 'user_currency')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_date):
        user = UserProfileInfo(
            email = validated_date['email'],
            username = validated_date['username'],
            plan_type = validated_date['plan_type'],
            user_country = validated_date['user_country'],
            user_currency = validated_date['user_currency']
        )
        user.set_password(validated_date['password']) #for hashing password
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.plan_type = validated_data.get('plan_type', instance.plan_type)
        instance.user_country = validated_data.get('user_country', instance.user_country)
        instance.user_currency = validated_data.get('user_currency', instance.user_currency)
        password = validated_data.get('password', None)
        if password: instance.set_password(password) #to hash the password
        instance.save()
        return instance