from django.db import models


class Kravat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    skidka = models.BooleanField(default=False, blank=True, null=True)
    image = models.ImageField(upload_to='media/kravat_images/', blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kravat"
        verbose_name_plural = "Kravat"


class Shkaf(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    boyi = models.CharField(max_length=100, blank=True, null=True)
    eni = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    skidka = models.BooleanField(default=False, blank=True, null=True)
    image = models.ImageField(upload_to='media/shkaf_images/', blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Shkaf"
        verbose_name_plural = "Shkaf"


class Prixoshka(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    boyi = models.CharField(max_length=100, blank=True, null=True)
    eni = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    skidka = models.BooleanField(default=False, blank=True, null=True)
    image = models.ImageField(upload_to='media/prixoshka_images/', blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Prixoshka"
        verbose_name_plural = "Prixoshka"


class Parta(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    boyi = models.CharField(max_length=100, blank=True, null=True)
    eni = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    skidka = models.BooleanField(default=False, blank=True, null=True)
    image = models.ImageField(upload_to='media/parta_images/', blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Parta"
        verbose_name_plural = "Parta"


class Tumba(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    boyi = models.CharField(max_length=100, blank=True, null=True)
    eni = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    skidka = models.BooleanField(default=False, blank=True, null=True)
    image = models.ImageField(upload_to='media/tumba_images/', blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tumba"
        verbose_name_plural = "Tumba"


class Podobuv(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    boyi = models.CharField(max_length=100, blank=True, null=True)
    eni = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    skidka = models.BooleanField(default=False, blank=True, null=True)
    image = models.ImageField(upload_to='media/podobuv_images/', blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Podobuv"
        verbose_name_plural = "Podobuv"