from django.db import models


class Place(models.Model):
    title = models.CharField('Компания', max_length=255)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Подробное описание')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')


    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Компания'
    )
    title = models.CharField(max_length=200, verbose_name='Компания')
    image = models.ImageField(verbose_name='Картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'




