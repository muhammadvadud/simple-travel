from rest_framework_simplejwt.views import TokenObtainPairView
from core.apps.accounts.serializers.login_phone import PhoneTokenObtainPairSerializer


class PhoneTokenObtainPairView(TokenObtainPairView):
    serializer_class = PhoneTokenObtainPairSerializer
