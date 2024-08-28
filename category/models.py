from django.db import models


class Kravat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=255, blank=True, null=True)
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
    price = models.CharField(max_length=255, blank=True, null=True)
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
    price = models.CharField(max_length=255, blank=True, null=True)
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
    price = models.CharField(max_length=255, blank=True, null=True)
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
    price = models.CharField(max_length=255, blank=True, null=True)
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
    price = models.CharField(max_length=255, blank=True, null=True)
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


class Image(models.Model):
    image = models.ImageField(upload_to='media/images/')
    kravat = models.ForeignKey(Kravat, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    shkaf = models.ForeignKey(Shkaf, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    prixoshka = models.ForeignKey(Prixoshka, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    parta = models.ForeignKey(Parta, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    tumba = models.ForeignKey(Tumba, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    podobuv = models.ForeignKey(Podobuv, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} for {self.kravat or self.shkaf or self.prixoshka or self.parta or self.tumba or self.podobuv}"
