from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=500, verbose_name="Заголовок")
    slug = models.CharField(max_length=150, verbose_name="slug", blank=True, null=True)
    content = models.TextField(verbose_name="Содержание", blank=True, null=True)
    preview = models.ImageField(
        upload_to="blog_preview/", verbose_name="Изображение", blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания", blank=True
    )
    is_public = models.BooleanField(default=False, verbose_name="Признак публикации")
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
