from django.contrib import admin

from category.models import Kravat, Shkaf, Prixoshka, Parta, Tumba, Podobuv


@admin.register(Kravat)
class KravatAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'price', 'skidka', 'image', 'order',)


@admin.register(Shkaf)
class ShkafAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'order',)


@admin.register(Prixoshka)
class PrixoshkaAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'order',)


@admin.register(Parta)
class PartaAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'order',)


@admin.register(Tumba)
class TumbaAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'order',)


@admin.register(Podobuv)
class PodobuvAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'order',)
