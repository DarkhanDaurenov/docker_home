from django.urls import path
from users.views import PaymentCreateAPIView, UsersCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('create-payment/', PaymentCreateAPIView.as_view(), name='create_payment'),
    path('register/', UsersCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]
