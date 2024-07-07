from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView
from users.models import Payment, User
from users.serializers import PaymentSerializer, UsersSerializer
from rest_framework.permissions import AllowAny


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['payment_date']
    search_fields = ['paid_course__title', 'paid_lesson__title', 'payment_method']


class UsersCreateAPIView(CreateAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()




