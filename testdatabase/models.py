from django.db import models
from django.contrib.postgres.fields import ArrayField


class Movie(models.Model):
    title = models.TextField('Название', null=True, blank=True)
    title_original = models.TextField('Оригинальное название', null=True, blank=True)
    year_start = models.IntegerField('Год выхода', null=True, blank=True)
    year_end = models.IntegerField('Последний год выхода', null=True, blank=True)
    categories = ArrayField(models.TextField(), verbose_name='Категории', null=True, blank=True)
    rating = models.FloatField('Рейтинг', null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    countries = ArrayField(models.TextField(), verbose_name='Страны', null=True, blank=True)
    url = models.URLField('Ссылка')
    date_now = models.DateTimeField('Дата выхода', null=True, blank=True)

    class Meta:
        db_table = 'test'
        managed = False

    def __str__(self):
        return self.title

    def __repr__(self):
        return Movie.__doc__

    def get_absolute_url(self):
        return f'/testdatabase/{self.id}'