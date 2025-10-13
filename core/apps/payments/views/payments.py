from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response

from core.apps.payments.serializers import PaymentSerializer


@extend_schema(tags=["payments"])
class PaymentLinkView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, payment_type):
        serializer = PaymentSerializer(
            data=request.data,
            context={"request": request, "payment_type": payment_type}
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
