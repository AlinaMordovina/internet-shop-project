from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="products_image/", verbose_name="Изображение", blank=True, null=True
    )
    category = models.ForeignKey(
        "catalog.Category",
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания", blank=True
    )
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата изменения", blank=True, null=True
    )
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name", "price")

    def __str__(self):
        return f"{self.name}: {self.price}руб."


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Продукт",
        related_name="versions",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    version_number = models.PositiveIntegerField(default=0, verbose_name="Номер версии")
    version_name = models.CharField(max_length=150, verbose_name="Название версии")
    is_active = models.BooleanField(
        default=False, verbose_name="Признак текущей версии"
    )

    def __str__(self):
        return (
            f"{self.product}: номер версии {self.version_number} ({self.version_name})"
        )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ("product", "version_number")
