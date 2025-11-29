from rest_framework import serializers


class LocationListSerializer(serializers.Serializer):
    departures = serializers.ListField(
        child=serializers.CharField()
    )
    destinations = serializers.ListField(
        child=serializers.CharField()
    )
