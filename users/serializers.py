from rest_framework import serializers
from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'paid_course', 'paid_lesson', 'payment_amount', 'payment_method', 'payment_date', 'link']
        read_only_fields = ['user', 'payment_date', 'link']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'phone', 'city', 'avatar']
        extra_kwargs = {
            'password': {'write_only': True}
        }

