from rest_framework import serializers

from category.models import Kravat, Shkaf, Prixoshka, Parta, Tumba, Podobuv


class KravatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kravat
        fields = ('id', 'name', 'description', 'price', 'skidka', 'image', 'created_at',
                  'updated_at',)


class ShkafSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shkaf
        fields = ('id', 'name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'created_at',
                  'updated_at',)


class PrixoshkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prixoshka
        fields = ('id', 'name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'created_at',
                  'updated_at',)


class PartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parta
        fields = ('id', 'name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'created_at',
                  'updated_at',)


class TumbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tumba
        fields = ('id', 'name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'created_at',
                  'updated_at',)


class PodobuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podobuv
        fields = ('id', 'name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'created_at',
                  'updated_at',)
