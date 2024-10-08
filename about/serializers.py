from rest_framework import serializers

from about.models import Slider, Location, Connection


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'title', 'image', 'created_at', 'updated_at',)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'title', 'created_at', 'updated_at',)


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ('id', 'telefon', 'email', 'telegram', 'instagram', 'facebook', 'created_at', 'updated_at',)

