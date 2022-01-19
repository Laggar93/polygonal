import os
import sys
import uuid
from io import BytesIO
from PIL import Image
from ckeditor.fields import RichTextField
from django.core.files.uploadedfile import InMemoryUploadedFile
from django_resized import ResizedImageField
from django.db import models
from pytils.translit import slugify

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


class advice_main(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500)
    name = models.CharField('Название заголовка', max_length=500)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Советы по сборке'
        verbose_name_plural = 'Советы по сборке'


class advice_page(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500)
    order = models.IntegerField('Порядок показа', null=True)
    is_active = models.BooleanField('Показывать на сайте', default=True)
    name = models.CharField('Название элемента', max_length=500)
    main_photo = ResizedImageField('Основное изображение', size=[2048, 1536], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                   help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.')
    main_photo_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xxl2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slug = models.SlugField('URL', max_length=50, allow_unicode=True, blank=True,
                            help_text='URL генерируется автоматически из названия раздела, но может быть задан вручную', unique=True)
    intro_text = RichTextField('Текст справа', blank=True)


    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Страница советов по сборке'
        verbose_name_plural = 'Страница советов по сборке'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.main_photo != self.main_photo:
            self.main_photo_xxl = resize_img(self.main_photo_xxl, self.main_photo, [1024, 768])
            self.main_photo_xxl2x = resize_img(self.main_photo_xxl2x, self.main_photo, [1600, 1200])
            self.main_photo_xs = resize_img(self.main_photo_xs, self.main_photo, [768, 576])
            self.main_photo_xs2 = resize_img(self.main_photo_xs2x, self.main_photo, [1536, 1152])
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        else:
            self.slug = slugify(self.slug)[:50]
        super().save(*args, **kwargs)


class advice_blocks(models.Model):
    advice_page = models.ForeignKey(advice_page, on_delete=models.CASCADE, verbose_name='Страница советов по сборке')
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500)
    order = models.IntegerField('Порядок показа', null=True)
    name = models.CharField('Заголовок блока', max_length=500)
    video_link = models.CharField('Ссылка на видео Vimeo или YouTube', max_length=500, blank=True)
    text = RichTextField('Текст', null=True, blank=True)
    title_paragraph1 = RichTextField('Первый заголовок пункта списка', null=True, blank=True)
    title_paragraph2 = RichTextField('Второй заголовок пункта списка', null=True, blank=True)
    title_paragraph3 = RichTextField('Третий заголовок пункта списка', null=True, blank=True)
    title_paragraph4 = RichTextField('Четвертый заголовок пункта списка', null=True, blank=True)
    title_paragraph5 = RichTextField('Пятый заголовок пункта списка', null=True, blank=True)
    text_paragraph1 = RichTextField('Текст первого пункта', null=True, blank=True)
    text_paragraph2 = RichTextField('Текст второго пункта', null=True, blank=True)
    text_paragraph3 = RichTextField('Текст третьего пункта', null=True, blank=True)
    text_paragraph4 = RichTextField('Текст четвертого пункта', null=True, blank=True)
    text_paragraph5 = RichTextField('Текст пятого пункта', null=True, blank=True)
    image = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_1 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_2 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_3 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_4 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_5 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_6 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_7 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_8 = models.ImageField(upload_to=get_file_path, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Блоки страницы советов'
        verbose_name_plural = 'Блоки страницы советов'
