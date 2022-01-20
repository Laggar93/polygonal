import os
import sys
import uuid
from io import BytesIO
from PIL import Image
from ckeditor.fields import RichTextField
from django.core.files.uploadedfile import InMemoryUploadedFile
from django_resized import ResizedImageField
from django.utils.functional import cached_property
from django.utils.html import format_html
from django.db import models


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    if ext == 'png' or ext == 'jpg' or ext == 'jpeg' or ext == 'svg':
        dir = 'images/'
    else:
        dir = 'files/'
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(dir, filename)

def resize_img(f1, f2, fs):
    f1 = f2
    image1 = f1
    img1 = Image.open(image1)
    new_img1 = img1.convert('RGB')
    ratio_current = new_img1.size[1] / new_img1.size[0]
    ratio_new = fs[1] / fs[0]
    if ratio_current <= ratio_new:
        new_width = (fs[1] * new_img1.size[0]) / new_img1.size[1]
        new_height = fs[1]
        resized_new_img1 = new_img1.resize((int(new_width), int(new_height)),Image.ANTIALIAS)
        box = ((resized_new_img1.size[0] - fs[0]) / 2, 0, resized_new_img1.size[0] - (resized_new_img1.size[0] - fs[0]) / 2,
               resized_new_img1.size[1])
        resized_new_img1 = resized_new_img1.crop(box)
    else:
        new_width = fs[0]
        new_height = (new_img1.size[1] * fs[0]) / new_img1.size[0]
        resized_new_img1 = new_img1.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        box = (0, (resized_new_img1.size[1] - fs[1]) / 2, 0, resized_new_img1.size[1] - (resized_new_img1.size[1] - fs[1]) / 2)
        resized_new_img1 = resized_new_img1.crop(box)
    filestream1 = BytesIO()
    resized_new_img1.save(filestream1, 'JPEG', quality=80)
    filestream1.seek(0)
    name1 = f"{f1.name}"
    return InMemoryUploadedFile(
        filestream1, 'ImageField', name1, 'jpeg/image',
        sys.getsizeof(filestream1), None
    )


class project_page(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500)
    projects = models.CharField('Стат. перевод - Проекты на заказ', max_length=255, blank=True)
    another_projects = models.CharField('Стат. перевод - Другие проекты', max_length=255, blank=True)
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
    first_display = models.BooleanField('Первый проект', default=False, unique=True)
    name = models.CharField('Название проекта', max_length=500)
    main_photo = ResizedImageField('Основное изображение', size=[2048, 1536], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                        help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.')
    main_photo_sm = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_original = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)


    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Список проектов'
        verbose_name_plural = 'Списки проектов'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.main_photo != self.main_photo:
            self.main_photo_sm = resize_img(self.main_photo_sm, self.main_photo, [1024, 768])
            self.main_photo_original = resize_img(self.main_photo_original, self.main_photo, [1600, 1200])
            self.main_photo_xs = resize_img(self.main_photo_xs, self.main_photo, [768, 576])
            self.main_photo_xs2x = resize_img(self.main_photo_xs2x, self.main_photo, [1536, 1152])

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="300">', img=self.main_photo.url)

    display_image.short_description = 'Предпросмотр'


class project_images(models.Model):
    project = models.ForeignKey(project_list, on_delete=models.CASCADE, related_name='gallery_images', verbose_name='Проекты на заказ')
    order = models.IntegerField('Порядок показа')
    main_photo = ResizedImageField('Основное изображение', size=[1600, 1200], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                        help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.')

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['order']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="300">', img=self.main_photo.url)

    display_image.short_description = 'Предпросмотр'
