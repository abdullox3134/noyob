from django.contrib import admin

from about.models import Slider, Location, Connection


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title', 'image', 'order',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title', 'lat', 'long',)


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('telefon', 'created_at', 'updated_at')
    search_fields = ('telefon',)
    fields = ('telefon', 'email', 'telegram', 'instagram', 'facebook',)

