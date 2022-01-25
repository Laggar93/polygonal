from django.db import models
from ckeditor.fields import RichTextField


class map_main(models.Model):
    is_active = models.BooleanField('Активная', default=True)
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500, blank=True)
    name = models.CharField('Название в меню', max_length=255, null=True)
    title_page = models.CharField('Заголовок страницы', max_length=500, null=True)
    bottom_text = models.CharField('Текст под заголовком', max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Где купить'
        verbose_name_plural = 'Где купить'


class map_town(models.Model):
    town = models.CharField('Город', max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.town)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Город'


class map_shop(models.Model):
    town = models.ForeignKey(map_town, verbose_name='Город', on_delete=models.CASCADE, related_name='map_towns')
    order = models.IntegerField('Порядок показа', null=True)
    name = models.CharField('Название', max_length=500, null=True)
    latitude = models.CharField('Широта', max_length=500, null=True)
    longitude = models.CharField('Долгота', max_length=500, null=True)
    info = RichTextField('Информация', blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

