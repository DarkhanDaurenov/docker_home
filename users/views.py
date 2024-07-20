from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import Payment, User
from users.serializers import PaymentSerializer, UsersSerializer
from users.services import create_stripe_product, create_stripe_price, create_stripe_session
from rest_framework import filters, status
from rest_framework.response import Response

class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['payment_date']
    search_fields = ['paid_course__title', 'paid_lesson__title', 'payment_method']


class PaymentCreateAPIView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product_id = create_stripe_product(f"Payment for {payment.paid_course or payment.paid_lesson}")
        price_id = create_stripe_price(product_id, payment.payment_amount)
        session_id, payment_link = create_stripe_session(
            price_id,
            success_url="https://127.0.0.1:8000/success",
            cancel_url="https://127.0.0.1:8000/cancel"
        )
        payment.link = payment_link
        payment.save()
        return Response({'session_id': session_id, 'payment_link': payment_link}, status=status.HTTP_201_CREATED)


class UsersCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


