from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products_image/', verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey("catalog.Category",
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 related_name='products'
                                 )
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения', blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name', 'price')

    def __str__(self):
        return f'{self.name}: {self.price}руб.'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name
