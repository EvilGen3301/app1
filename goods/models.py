from tabnanny import verbose
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="სახელი")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "კატეგორია"
        verbose_name_plural = "კატეგორიები"

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="სახელი")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="აღწერა")
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name="გამოსახულება")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="ფასი")
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="ფასდაკლება % -ში")
    quantity = models.PositiveIntegerField(default=0, verbose_name='რაოდენობა')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="კატეგორია")
    class Meta:
        db_table = "product"
        verbose_name = "პროდუქტი"
        verbose_name_plural = "პროდუქტები"

    def __str__(self) -> str:
        return f'{self.name} რაოდენობა - {self.quantity}'
    
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self):
        if self.discount:
            return round(self.price  - self.price * self.discount / 100, 2)
        else:
            return self.price





