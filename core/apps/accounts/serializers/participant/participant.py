from rest_framework import serializers

from core.apps.accounts.models import ParticipantModel, ParticipantPasportImageModel


class ParticipantPasportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantPasportImageModel
        fields = ["image"]


class BaseParticipantSerializer(serializers.ModelSerializer):
    participant_pasport_image = ParticipantPasportImageSerializer(many=True, read_only=True)

    class Meta:
        model = ParticipantModel
        fields = [
            "id",
            "first_name",
            "last_name",
            "birth_date",
            "phone_number",
            "gender",
            "participant_pasport_image",

        ]


class ListParticipantSerializer(BaseParticipantSerializer):
    class Meta(BaseParticipantSerializer.Meta):
        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class RetrieveParticipantSerializer(BaseParticipantSerializer):
    class Meta(BaseParticipantSerializer.Meta): ...


class CreateParticipantSerializer(BaseParticipantSerializer):
    pasport_images = serializers.ListField(child=serializers.ImageField(), write_only=True, required=True)

    class Meta(BaseParticipantSerializer.Meta):
        fields = [
            "id",
            "pasport_images",
            "first_name",
            "last_name",
            "birth_date",
            "gender",
            "phone_number",
        ]

    def create(self, validated_data):
        pasport_images = validated_data.pop("pasport_images", [])
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            validated_data["created_by_id"] = request.user.id
        participant = ParticipantModel.objects.create(**validated_data)
        if pasport_images:
            for pasport_image in pasport_images:
                ParticipantPasportImageModel.objects.create(image=pasport_image, participant=participant)
        return participant
