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


class Blog(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', blank=True, null=True)
    content = models.TextField(verbose_name='Содержание', blank=True, null=True)
    preview = models.ImageField(upload_to='blog_preview/', verbose_name='Изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', blank=True)
    is_public = models.BooleanField(default=False, verbose_name='Признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
