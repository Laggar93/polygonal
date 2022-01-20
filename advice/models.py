import os
import sys
import uuid
from io import BytesIO
from PIL import Image
from ckeditor.fields import RichTextField
from django.core.files.uploadedfile import InMemoryUploadedFile
from django_resized import ResizedImageField
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.html import format_html
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
    advice = models.CharField('Советы по сборке', max_length=255, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Советы по сборке'
        verbose_name_plural = 'Советы по сборке'


class advice_page(models.Model):

    is_active = models.BooleanField('Показывать на сайте', default=True)
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500)
    order = models.IntegerField('Порядок показа', null=True)
    name = models.CharField('Название элемента', max_length=500)
    main_photo_xxl2x = ResizedImageField('Основное изображение', size=[1600, 1200], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                   help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.')
    main_photo_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slug = models.SlugField('URL', max_length=50, allow_unicode=True, blank=True,
                            help_text='URL генерируется автоматически из названия раздела, но может быть задан вручную', unique=True)
    intro_text = RichTextField('Вступительный текст', blank=True)

    __original_main_photo_xxl2 = None
    
    def __init__(self, *args, **kwargs):
        super(advice_page, self).__init__(*args, **kwargs)
        self.__original_main_photo_xxl2 = self.main_photo_xxl2x


    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Список советов'
        verbose_name_plural = 'Список советов'

    def get_absolute_url(self):
        return reverse('advice_item_view', kwargs={'advice_page_slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.__original_main_photo_xxl2 != self.main_photo_xxl2x:
            self.main_photo_xxl = resize_img(self.main_photo_xxl, self.main_photo_xxl2x, [800, 600])
            self.main_photo_xs = resize_img(self.main_photo_xs, self.main_photo_xxl2x, [728, 546])
            self.main_photo_xs2x = resize_img(self.main_photo_xs2x, self.main_photo_xxl2x, [1456, 1092])
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        else:
            self.slug = slugify(self.slug)[:50]
        super().save(*args, **kwargs)

    @cached_property
    def display_page_image(self):
        return format_html('<img src="{img}" width="300">', img=self.main_photo_xxl2x.url)

    display_page_image.short_description = 'Предпросмотр'


class advice_blocks(models.Model):
    advice_page = models.ForeignKey(advice_page, on_delete=models.CASCADE, verbose_name='Страница советов по сборке')
    order = models.IntegerField('Порядок показа', null=True)
    name = models.CharField('Заголовок блока', max_length=500)
    video_link = models.CharField('Ссылка на видео Vimeo или YouTube', max_length=500, blank=True)
    top_text = RichTextField('Верхний текст', null=True, blank=True)
    bottom_text = RichTextField('Нижний текст', null=True, blank=True)
    title_paragraph1 = models.CharField('Первый заголовок пункта списка', max_length=255, null=True, blank=True)
    title_paragraph2 = models.CharField('Второй заголовок пункта списка', max_length=255, null=True, blank=True)
    title_paragraph3 = models.CharField('Третий заголовок пункта списка', max_length=255, null=True, blank=True)
    title_paragraph4 = models.CharField('Четвертый заголовок пункта списка', max_length=255, null=True, blank=True)
    title_paragraph5 = models.CharField('Пятый заголовок пункта списка', max_length=255, null=True, blank=True)
    text_paragraph1 = RichTextField('Текст первого пункта', null=True, blank=True)
    text_paragraph2 = RichTextField('Текст второго пункта', null=True, blank=True)
    text_paragraph3 = RichTextField('Текст третьего пункта', null=True, blank=True)
    text_paragraph4 = RichTextField('Текст четвертого пункта', null=True, blank=True)
    text_paragraph5 = RichTextField('Текст пятого пункта', null=True, blank=True)
    image = ResizedImageField('Одно изображение', size=[1600, 1200], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                   help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    
    slide_picture_1_xxl2x = ResizedImageField('Изображение 1 для слайдера', size=[2400, 1800], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                   help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    slide_picture_1_original = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_1_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_1_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_1_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_2_xxl2x = ResizedImageField('Изображение 1 для слайдера', size=[2400, 1800], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                              help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    slide_picture_2_original = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_2_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_2_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_2_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_3_xxl2x = ResizedImageField('Изображение 1 для слайдера', size=[2400, 1800], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                              help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    slide_picture_3_original = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_3_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_3_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_3_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_4_xxl2x = ResizedImageField('Изображение 1 для слайдера', size=[2400, 1800], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                              help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    slide_picture_4_original = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_4_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_4_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_4_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_5_xxl2x = ResizedImageField('Изображение 1 для слайдера', size=[2400, 1800], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                              help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    slide_picture_5_original = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_5_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_5_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_5_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_6_xxl2x = ResizedImageField('Изображение 1 для слайдера', size=[2400, 1800], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                              help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    slide_picture_6_original = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_6_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_6_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_6_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_7_xxl2x = ResizedImageField('Изображение 1 для слайдера', size=[2400, 1800], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                              help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    slide_picture_7_original = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_7_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_7_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    slide_picture_7_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    __original_slide_picture_1_xxl2x = None
    __original_slide_picture_2_xxl2x = None
    __original_slide_picture_3_xxl2x = None
    __original_slide_picture_4_xxl2x = None
    __original_slide_picture_5_xxl2x = None
    __original_slide_picture_6_xxl2x = None
    __original_slide_picture_7_xxl2x = None

    def __init__(self, *args, **kwargs):
        super(advice_blocks, self).__init__(*args, **kwargs)
        self.__original_slide_picture_1_xxl2x = self.slide_picture_1_xxl2x
        self.__original_slide_picture_2_xxl2x = self.slide_picture_2_xxl2x
        self.__original_slide_picture_3_xxl2x = self.slide_picture_3_xxl2x
        self.__original_slide_picture_4_xxl2x = self.slide_picture_4_xxl2x
        self.__original_slide_picture_5_xxl2x = self.slide_picture_5_xxl2x
        self.__original_slide_picture_6_xxl2x = self.slide_picture_6_xxl2x
        self.__original_slide_picture_7_xxl2x = self.slide_picture_7_xxl2x

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Блоки страницы советов'
        verbose_name_plural = 'Блоки страницы советов'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.slide_picture_1_xxl2x != self.__original_slide_picture_1_xxl2x:
            self.slide_picture_1_original = resize_img(self.slide_picture_1_original, self.slide_picture_1_xxl2x, [800, 600])
            self.slide_picture_1_xxl = resize_img(self.slide_picture_1_xxl, self.slide_picture_1_xxl2x, [728, 546])
            self.slide_picture_1_xs2x = resize_img(self.slide_picture_1_xs2x, self.slide_picture_1_xxl2x, [1456, 1092])
            self.slide_picture_1_xs = resize_img(self.slide_picture_1_xs, self.slide_picture_1_xxl2x, [1456, 1092])
        if self.slide_picture_2_xxl2x != self.__original_slide_picture_2_xxl2x:
            self.slide_picture_2_original = resize_img(self.slide_picture_2_original, self.slide_picture_2_xxl2x, [800, 600])
            self.slide_picture_2_xxl = resize_img(self.slide_picture_2_xxl, self.slide_picture_2_xxl2x, [728, 546])
            self.slide_picture_2_xs2x = resize_img(self.slide_picture_2_xs2x, self.slide_picture_2_xxl2x, [1456, 1092])
            self.slide_picture_2_xs = resize_img(self.slide_picture_2_xs, self.slide_picture_2_xxl2x, [1456, 1092])
        if self.slide_picture_3_xxl2x != self.__original_slide_picture_3_xxl2x:
            self.slide_picture_3_original = resize_img(self.slide_picture_3_original, self.slide_picture_3_xxl2x, [800, 600])
            self.slide_picture_3_xxl = resize_img(self.slide_picture_3_xxl, self.slide_picture_3_xxl2x, [728, 546])
            self.slide_picture_3_xs2x = resize_img(self.slide_picture_3_xs2x, self.slide_picture_3_xxl2x, [1456, 1092])
            self.slide_picture_3_xs = resize_img(self.slide_picture_3_xs, self.slide_picture_3_xxl2x, [1456, 1092])
        if self.slide_picture_4_xxl2x != self.__original_slide_picture_4_xxl2x:
            self.slide_picture_4_original = resize_img(self.slide_picture_4_original, self.slide_picture_4_xxl2x, [800, 600])
            self.slide_picture_4_xxl = resize_img(self.slide_picture_4_xxl, self.slide_picture_4_xxl2x, [728, 546])
            self.slide_picture_4_xs2x = resize_img(self.slide_picture_4_xs2x, self.slide_picture_4_xxl2x, [1456, 1092])
            self.slide_picture_4_xs = resize_img(self.slide_picture_4_xs, self.slide_picture_4_xxl2x, [1456, 1092])
        if self.slide_picture_5_xxl2x != self.__original_slide_picture_5_xxl2x:
            self.slide_picture_5_original = resize_img(self.slide_picture_5_original, self.slide_picture_5_xxl2x, [800, 600])
            self.slide_picture_5_xxl = resize_img(self.slide_picture_5_xxl, self.slide_picture_5_xxl2x, [728, 546])
            self.slide_picture_5_xs2x = resize_img(self.slide_picture_5_xs2x, self.slide_picture_5_xxl2x, [1456, 1092])
            self.slide_picture_5_xs = resize_img(self.slide_picture_5_xs, self.slide_picture_5_xxl2x, [1456, 1092])
        if self.slide_picture_6_xxl2x != self.__original_slide_picture_6_xxl2x:
            self.slide_picture_6_original = resize_img(self.slide_picture_6_original, self.slide_picture_6_xxl2x, [800, 600])
            self.slide_picture_6_xxl = resize_img(self.slide_picture_6_xxl, self.slide_picture_6_xxl2x, [728, 546])
            self.slide_picture_6_xs2x = resize_img(self.slide_picture_6_xs2x, self.slide_picture_6_xxl2x, [1456, 1092])
            self.slide_picture_6_xs = resize_img(self.slide_picture_6_xs, self.slide_picture_6_xxl2x, [1456, 1092])
        if self.slide_picture_7_xxl2x != self.__original_slide_picture_7_xxl2x:
            self.slide_picture_7_original = resize_img(self.slide_picture_7_original, self.slide_picture_7_xxl2x, [800, 600])
            self.slide_picture_7_xxl = resize_img(self.slide_picture_7_xxl, self.slide_picture_7_xxl2x, [728, 546])
            self.slide_picture_7_xs2x = resize_img(self.slide_picture_7_xs2x, self.slide_picture_7_xxl2x, [1456, 1092])
            self.slide_picture_7_xs = resize_img(self.slide_picture_7_xs, self.slide_picture_7_xxl2x, [1456, 1092])
        super().save(*args, **kwargs)

    @cached_property
    def display_block_image(self):
        return format_html('<img src="{img}" width="300">', img=self.image.url)

    display_block_image.short_description = 'Предпросмотр'
