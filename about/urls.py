from django.urls import path

from about.views import SliderListView, sliderdetail, LocationListView, locationdetail, ConnectionListView, \
    connectiondetail, CardListView, carddetail

urlpatterns = [
    path('slider/', SliderListView.as_view(), name='slider-list'),
    path('slider/<int:pk>/', sliderdetail, name='slider-detail'),

    path('location/', LocationListView.as_view(), name='location-list'),
    path('location/<int:pk>/', locationdetail, name='location-detail'),

    path('connection/', ConnectionListView.as_view(), name='connection-list'),
    path('connection/<int:pk>/', connectiondetail, name='connection-detail'),

    path('card/', CardListView.as_view(), name='card-list'),
    path('card/<int:pk>/', carddetail, name='card-detail'),
]
