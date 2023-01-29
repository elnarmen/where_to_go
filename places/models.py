from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Компания', max_length=255)
    description_short = models.TextField('Краткое описание')
    description_long = HTMLField('Подробное описание')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Локация'
    )
    image = models.ImageField(verbose_name='Картинка')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.order} {self.place.title}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['order']
        unique_together = ['place', 'order']
