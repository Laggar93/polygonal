# from PIL import Image
import os
import uuid
from ckeditor.fields import RichTextField
from django.db import models


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    if ext == 'png' or ext == 'jpg' or ext == 'jpeg' or ext == 'svg':
        dir = 'images/'
    else:
        dir = 'files/'
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(dir, filename)


class project_page(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500)
    name = models.CharField('Название раздела', max_length=500)
    text = RichTextField('Текст после названия', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Проекты на заказ'
        verbose_name_plural = 'Проекты на заказ'


class project_list(models.Model):
    order = models.IntegerField('Порядок показа')
    is_active = models.BooleanField('Показывать на сайте', default=True)

    # сделать unique boolean для обозначения, что проект первый

    name = models.CharField('Название проекта', max_length=500)

    # превью: 5 размеров (sm, sm2x, xs, xs2x), 1 изображение будет ResizedImageField, остальные ImageField

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Список проектов'
        verbose_name_plural = 'Списки проектов'


class project_images(models.Model):
    project = models.ForeignKey(project_list, on_delete=models.CASCADE, verbose_name='Проекты на заказ')
    order = models.IntegerField('Порядок показа')

    main_photo_1 = models.ImageField(upload_to=get_file_path, blank=True, null=True)

    # 1 изображение ResizedImageField

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['order']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
