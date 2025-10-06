from rest_framework_simplejwt.views import TokenObtainPairView
from core.apps.accounts.serializers.email_register.login_email import  EmailTokenObtainPairSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
