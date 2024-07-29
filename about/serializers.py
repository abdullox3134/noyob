from rest_framework import serializers

from about.models import Slider, Location, Connection, Card


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'title', 'image', 'created_at', 'updated_at',)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'title', 'lat', 'long', 'created_at', 'updated_at',)


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ('id', 'telefon', 'email', 'telegram', 'instagram', 'facebook', 'created_at', 'updated_at',)


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'card_1', 'card_1_name', 'card_2', 'card_2_name', 'card_3', 'card_3_name', 'created_at',
                  'updated_at',)
