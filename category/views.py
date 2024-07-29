from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from category.models import Kravat, Shkaf, Prixoshka, Parta, Tumba, Podobuv
from category.serializers import KravatSerializer, ShkafSerializer, PrixoshkaSerializer, PartaSerializer, \
    TumbaSerializer, PodobuvSerializer


class KravatListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = KravatSerializer

    def get_queryset(self):
        return Kravat.objects.all().order_by('order')


@api_view(['GET'])
def kravatdetail(request, pk):
    kravat = get_object_or_404(Kravat, pk=pk)
    serializer = KravatSerializer(kravat, context={'request': request})
    return Response(serializer.data)


class ShkafListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ShkafSerializer

    def get_queryset(self):
        return Shkaf.objects.all().order_by('order')


@api_view(['GET'])
def shkafdetail(request, pk):
    shkaf = get_object_or_404(Shkaf, pk=pk)
    serializer = ShkafSerializer(shkaf, context={'request': request})
    return Response(serializer.data)


class PrixoshkaListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = PrixoshkaSerializer

    def get_queryset(self):
        return Prixoshka.objects.all().order_by('order')


@api_view(['GET'])
def prixoshkadetail(request, pk):
    prixoshka = get_object_or_404(Prixoshka, pk=pk)
    serializer = PrixoshkaSerializer(prixoshka, context={'request': request})
    return Response(serializer.data)


class PartaListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = PartaSerializer

    def get_queryset(self):
        return Parta.objects.all().order_by('order')


@api_view(['GET'])
def partadetail(request, pk):
    parta = get_object_or_404(Parta, pk=pk)
    serializer = PartaSerializer(parta, context={'request': request})
    return Response(serializer.data)


class TumbaListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = TumbaSerializer

    def get_queryset(self):
        return Tumba.objects.all().order_by('order')


@api_view(['GET'])
def tumbadetail(request, pk):
    tumba = get_object_or_404(Tumba, pk=pk)
    serializer = TumbaSerializer(tumba, context={'request': request})
    return Response(serializer.data)


class PodobuvListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = PodobuvSerializer

    def get_queryset(self):
        return Podobuv.objects.all().order_by('order')


@api_view(['GET'])
def podobuvdetail(request, pk):
    podobuv = get_object_or_404(Podobuv, pk=pk)
    serializer = PodobuvSerializer(podobuv, context={'request': request})
    return Response(serializer.data)