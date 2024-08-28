from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/slider_images/')
    order = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'


class Location(models.Model):
    title = models.CharField(max_length=200)
    # lat = models.DecimalField(max_digits=22, decimal_places=18, default=0)
    # long = models.DecimalField(max_digits=22, decimal_places=18, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class Connection(models.Model):
    telefon = models.CharField(max_length=200)
    email = models.EmailField()
    telegram = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.telefon

    class Meta:
        verbose_name = 'Connection'
        verbose_name_plural = 'Connections'

