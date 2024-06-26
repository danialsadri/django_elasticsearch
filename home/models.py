from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ')
    author = models.CharField(max_length=100, verbose_name='نویسنده')
    description = models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'

    def __str__(self):
        return self.name
