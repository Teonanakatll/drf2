from django.db import models


class Women(models.Model):
    title = models.CharField('Имя', max_length=255)
    content = models.TextField('Описание', blank=True)
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    time_update = models.DateTimeField('Дата изменения', auto_now=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField('Имя', max_length=100, db_index=True)

    def __str__(self):
        return self.name
