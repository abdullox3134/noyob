from django.contrib import admin
from .models import Kravat, Shkaf, Prixoshka, Parta, Tumba, Podobuv, Image


class KravatImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image',)


class ShkafImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image',)


class PrixoshkaImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image',)


class PartaImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image',)


class TumbaImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image',)


class PodobuvImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image',)


@admin.register(Kravat)
class KravatAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'price', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'price', 'skidka', 'image', 'order',)
    inlines = [KravatImageInline]


@admin.register(Shkaf)
class ShkafAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'price', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'order',)
    inlines = [ShkafImageInline]


@admin.register(Prixoshka)
class PrixoshkaAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'price', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'order',)
    inlines = [PrixoshkaImageInline]


@admin.register(Parta)
class PartaAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'price', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'order',)
    inlines = [PartaImageInline]


@admin.register(Tumba)
class TumbaAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'price', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'order',)
    inlines = [TumbaImageInline]


@admin.register(Podobuv)
class PodobuvAdmin(admin.ModelAdmin):
    list_display = ('name', 'skidka', 'order', 'price', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name', 'description', 'boyi', 'eni', 'price', 'skidka', 'image', 'order',)
    inlines = [PodobuvImageInline]
