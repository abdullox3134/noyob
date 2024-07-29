from django.urls import path

from category.views import KravatListView, kravatdetail, ShkafListView, shkafdetail, PrixoshkaListView, prixoshkadetail, \
    PartaListView, partadetail, TumbaListView, tumbadetail, PodobuvListView, podobuvdetail

urlpatterns = [
    path('kravat/', KravatListView.as_view(), name='kravat-list'),
    path('kravat/<int:pk>/', kravatdetail, name='kravat-detail'),

    path('shkaf/', ShkafListView.as_view(), name='shkaf-list'),
    path('shkaf/<int:pk>/', shkafdetail, name='shkaf-detail'),

    path('prixoshka/', PrixoshkaListView.as_view(), name='prixoshka-list'),
    path('prixoshka/<int:pk>/', prixoshkadetail, name='prixoshka-detail'),

    path('parta/', PartaListView.as_view(), name='parta-list'),
    path('parta/<int:pk>/', partadetail, name='parta-detail'),

    path('tumba/', TumbaListView.as_view(), name='tumba-list'),
    path('tumba/<int:pk>/', tumbadetail, name='tumba-detail'),

    path('podobuv/', PodobuvListView.as_view(), name='podobuv-list'),
    path('podobuv/<int:pk>/', podobuvdetail, name='podobuv-detail'),
]
