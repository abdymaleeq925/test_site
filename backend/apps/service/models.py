from django.db import models

from backend.apps.accounts.models import User

class Product(models.Model):
    name = models.CharField("Название продукта", max_length=200)
    description = models.TextField("Описание продукта")
    price = models.DecimalField("Цена продукта", max_digits=8, decimal_places=1)
    image = models.ImageField("Фото", upload_to="product_images/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField("Активный", default=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created']
    
    def __str__(self):
        return self.name