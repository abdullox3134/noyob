from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from about.models import Slider, Location, Connection
from about.serializers import SliderSerializer, LocationSerializer, ConnectionSerializer


class SliderListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SliderSerializer

    def get_queryset(self):
        return Slider.objects.all().order_by('order')


@api_view(['GET'])
def sliderdetail(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    serializer = SliderSerializer(slider, context={'request': request})
    return Response(serializer.data)


class LocationListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.all()


@api_view(['GET'])
def locationdetail(request, pk):
    location = get_object_or_404(Location, pk=pk)
    serializer = LocationSerializer(location, context={'request': request})
    return Response(serializer.data)


class ConnectionListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ConnectionSerializer

    def get_queryset(self):
        return Connection.objects.all()


@api_view(['GET'])
def connectiondetail(request, pk):
    connection = get_object_or_404(Connection, pk=pk)
    serializer = ConnectionSerializer(connection, context={'request': request})
    return Response(serializer.data)
