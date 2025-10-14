from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.response import Response
from core.apps.tickets.filters import TicketsFilter
from core.apps.tickets.models import TicketorderModel, TicketsModel
from core.apps.tickets.permissions.tickets import TicketorderPermission
from core.apps.tickets.serializers.tickets import (
    CreateTicketorderSerializer,
    CreateTicketsSerializer,
    ListTicketorderSerializer,
    ListTicketsSerializer,
    RetrieveTicketorderSerializer,
    RetrieveTicketsSerializer,
    BaseTicketorderSerializer,
    FullInformationTicketsSerializer,
    GetTicketInfoOrderCreateSerializer,
    GetOrderPdfSerializer,
)


@extend_schema(tags=["tickets"])
class TicketsView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TicketsModel.objects.all().order_by("-id")
    serializer_class = FullInformationTicketsSerializer
    filterset_class = TicketsFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": FullInformationTicketsSerializer,
        "retrieve": RetrieveTicketsSerializer,
        "create": CreateTicketsSerializer,
    }

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        pagination_queryset = self.paginate_queryset(queryset)
        serializer = FullInformationTicketsSerializer(pagination_queryset, context={"request": request})
        response = self.get_paginated_response(serializer.data)
        return response


@extend_schema(tags=["ticketorder"])
class TicketorderView(BaseViewSetMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      GenericViewSet):
    queryset = TicketorderModel.objects.all()
    serializer_class = BaseTicketorderSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTicketorderSerializer,
        "retrieve": RetrieveTicketorderSerializer,
        "create": CreateTicketorderSerializer,
    }


@extend_schema(tags=["ticketorder"])
class GetTicketInfoOrderCreateView(BaseViewSetMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = GetTicketInfoOrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return TicketsModel.objects.filter(pk=pk)


@extend_schema(tags=["ticketorder"])
class GetOrderPdfView(APIView):
    permission_classes = [TicketorderPermission]

    def post(self, request, *args, **kwargs):
        serializer = GetOrderPdfSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(result)
