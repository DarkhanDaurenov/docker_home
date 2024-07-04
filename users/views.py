from rest_framework import filters
from rest_framework.generics import ListAPIView
from users.models import Payment
from users.serializers import PaymentSerializer

class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['payment_date']
    search_fields = ['paid_course__title', 'paid_lesson__title', 'payment_method']


