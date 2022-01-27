from ckeditor.fields import RichTextField
from django.db import models


class footer_elements(models.Model):
    with_love = models.CharField('Сделано с любовью в', max_length=255, null=True)
    year = models.PositiveIntegerField('Текущий год', default=1, null=True)

    def __str__(self):
        return str(self.with_love)

    class Meta:
        verbose_name = 'Текущий год и копирайт'
        verbose_name_plural = 'Текущий год и копирайт'


class rules(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500, blank=True)
    name = models.CharField('Название', max_length=255, null=True)
    text = models.TextField('Текст после названия', blank=True, null=True)
    info = RichTextField('Информация', blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Правила пользования'
        verbose_name_plural = 'Правила пользования'


class offer(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500, blank=True)
    name = models.CharField('Название', max_length=255, null=True)
    text = models.TextField('Текст после названия', blank=True, null=True)
    info = RichTextField('Информация', blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Публичная оферта'
        verbose_name_plural = 'Публичная оферта'



class policy(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500, blank=True)
    name = models.CharField('Название', max_length=255, null=True)
    info = RichTextField('Информация', blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Политика персональных данных'
        verbose_name_plural = 'Политика персональных данных'

