from rest_framework import serializers

from core.apps.accounts.models import ParticipantModel


class BaseParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantModel
        fields = [
            "id",
            "first_name",
            "last_name",

        ]


class ListParticipantSerializer(BaseParticipantSerializer):
    class Meta(BaseParticipantSerializer.Meta): ...


class RetrieveParticipantSerializer(BaseParticipantSerializer):
    class Meta(BaseParticipantSerializer.Meta): ...


class CreateParticipantSerializer(BaseParticipantSerializer):
    class Meta(BaseParticipantSerializer.Meta):
        fields = [
            "id",
        ]
