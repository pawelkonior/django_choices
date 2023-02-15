from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Subcategories'


class Product(models.Model):
    name = models.CharField(max_length=50)
    prize = models.DecimalField(decimal_places=2, max_digits=9)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    subcategory = models.ManyToManyField('SubCategory', related_name='products')

    def __str__(self):
        return self.name
