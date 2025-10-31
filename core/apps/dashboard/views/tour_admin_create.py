from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices.user import RoleChoice
from ..permission import IsModeratorOrBuxgalter, IsModeratorOrOperator
from ..permission.tour_agency import IsOperatorOrModerator
from ..permission.general_permission import IsModerator
from ..serializers.tour_admin_create import UpdateTourAdminPasswordSerializer, \
    CreateTourAdminSerializer, ListTourAdminSerializer
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from core.apps.accounts.models import TravelAgency


@extend_schema(tags=["Dashboard-TourAdmin"])
class TourAdminViewSet(BaseViewSetMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = get_user_model().objects.filter(role__in=[RoleChoice.TourAdmin]).order_by("-id")
    permission_classes = [IsOperatorOrModerator]
    http_method_names = ["get", "post", "delete", "head", "options"]

    action_permission_classes = {
    }
    action_serializer_class = {
    }

    @action(
        detail=True,
        methods=["get"],
        url_path="list",
        permission_classes=[IsModeratorOrOperator]
    )
    def list_agency_admins(self, request, pk=None):
        agency = get_object_or_404(TravelAgency, pk=pk)

        admins = get_user_model().objects.filter(
            travel_agency=agency,
            role=RoleChoice.TourAdmin
        ).order_by("-id")

        serializer = ListTourAdminSerializer(admins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], url_path="create", permission_classes=[IsModerator])
    def create_for_agency(self, request, pk=None):
        serializer = CreateTourAdminSerializer(
            data=request.data,
            context={"request": request, "pk": pk},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"], url_path="update", permission_classes=[IsOperatorOrModerator])
    def update_for_agency_password(self, request, pk=None):
        user = get_object_or_404(get_user_model(), pk=pk)
        serializer = UpdateTourAdminPasswordSerializer(
            instance=user,
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
