from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.tickets.models import TicketsModel
from ...serializers import UpdateFeaturedTicketSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["TicketFeatured"])
class UpdateFeaturedTicketAPIView(APIView):
    permission_classes = [IsModerator]


    def post(self, request, *args, **kwargs):
        ticket_id = kwargs.get("id")
        value = kwargs.get("value")

        serializer = UpdateFeaturedTicketSerializer(
            data={},
            context={
                "ticket_id": ticket_id,
                "value": value,
            }
        )
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(result, status=status.HTTP_200_OK)
