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
from django.http import HttpResponse, Http404
from rest_framework.exceptions import ValidationError
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
import os


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
    serializer_class = BaseTicketorderSerializer
    permission_classes = [TicketorderPermission]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTicketorderSerializer,
        "retrieve": RetrieveTicketorderSerializer,
        "create": CreateTicketorderSerializer,
    }

    def get_queryset(self):
        queryset = TicketorderModel.objects.filter(user=self.request.user)
        return queryset


@extend_schema(tags=["ticketorder"])
class GetTicketInfoOrderCreateView(BaseViewSetMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = GetTicketInfoOrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            raise ValidationError("Ticket id required")
        return TicketsModel.objects.filter(pk=pk)


@extend_schema(tags=["ticketorder"])
class GetOrderPdfView(APIView):
    permission_classes = [TicketorderPermission]

    def post(self, request, *args, **kwargs):
        serializer = GetOrderPdfSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        file_path = result.get("file_path") or result
        if not os.path.exists(file_path):
            return Response({"detail": "PDF fayl topilmadi."}, status=404)
        file_name = os.path.basename(file_path)
        with open(file_path, "rb") as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type="application/pdf")
            response["Content-Disposition"] = f'attachment; filename="{file_name}"'
            return response
