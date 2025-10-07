from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins, status

from core.apps.accounts.models import LikesModel
from core.apps.accounts.serializers.likes import CreateLikesSerializer, ListLikesSerializer, RetrieveLikesSerializer, \
    BaseLikesSerializer


@extend_schema(tags=["likes"])
class LikesView(BaseViewSetMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                GenericViewSet):
    queryset = LikesModel.objects.all()
    serializer_class = ListLikesSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListLikesSerializer,
        "retrieve": RetrieveLikesSerializer,
        "create": CreateLikesSerializer,
    }

    def get_queryset(self):
        user = self.request.user
        return LikesModel.objects.filter(user=user)

    def destroy(self, request, pk=None, *args, **kwargs):

        try:
            deleted_count, _ = self.get_queryset().filter(ticket_id=pk).delete()

            if deleted_count == 0:
                return Response({"detail": "Like topilmadi"}, status=status.HTTP_404_NOT_FOUND)

            return Response({"detail": "Like o'chirildi"}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
