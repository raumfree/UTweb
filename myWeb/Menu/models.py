from django.db import models
from django.urls import reverse


class Categories(models.Model):
    category = models.CharField(max_length=20, verbose_name='Категории')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


class Items(models.Model):
    item = models.CharField(max_length=20, verbose_name='Имя объекта')
    cat = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name='Категория')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.item

    def get_url(self):
        return reverse('content', kwargs={'content_slug': self.slug})

    class Meta:
        verbose_name = "Подпункты"
        verbose_name_plural = "Подпункты"

