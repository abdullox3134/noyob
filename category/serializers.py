from rest_framework import serializers
from category.models import Kravat, Shkaf, Prixoshka, Parta, Tumba, Podobuv, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image',)


class KravatSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Kravat
        fields = ('id', 'name', 'description', 'price', 'skidka', 'image', 'images', 'created_at', 'updated_at',)


class ShkafSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Shkaf
        fields = ('id', 'name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'images', 'created_at', 'updated_at',)


class PrixoshkaSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Prixoshka
        fields = ('id', 'name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'images', 'created_at', 'updated_at',)


class PartaSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Parta
        fields = ('id', 'name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'images', 'created_at', 'updated_at',)


class TumbaSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Tumba
        fields = ('id', 'name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'images', 'created_at', 'updated_at',)


class PodobuvSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Podobuv
        fields = ('id', 'name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'images', 'created_at', 'updated_at',)
