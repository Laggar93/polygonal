import os
import sys
import uuid
from io import BytesIO
from ckeditor.fields import RichTextField
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django_resized import ResizedImageField


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
        resized_new_img1 = new_img1.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        box = ((resized_new_img1.size[0] - fs[0]) / 2, 0, resized_new_img1.size[0] - (resized_new_img1.size[0] - fs[0]) / 2, resized_new_img1.size[1])
        resized_new_img1 = resized_new_img1.crop(box)
    else:
        new_width = fs[0]
        new_height = (new_img1.size[1] * fs[0]) / new_img1.size[0]
        resized_new_img1 = new_img1.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        box = (0, (resized_new_img1.size[1] - fs[1]) / 2, resized_new_img1.size[0], resized_new_img1.size[1] - (resized_new_img1.size[1] - fs[1]) / 2)
        resized_new_img1 = resized_new_img1.crop(box)
    filestream1 = BytesIO()
    resized_new_img1.save(filestream1, 'JPEG', quality=80)
    filestream1.seek(0)
    name1 = f"{f1.name}"
    return InMemoryUploadedFile(
        filestream1, 'ImageField', name1, 'jpeg/image',
        sys.getsizeof(filestream1), None
    )


class about_main(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500, blank=True)
    name = models.CharField('Название в меню', max_length=255, null=True)
    title_page = models.CharField('Заголовок страницы', max_length=500, null=True)
    bottom_text = models.CharField('Текст под заголовком страницы', max_length=500, null=True)
    main_photo_xl2x = ResizedImageField('Картинка в "О нас"', size=[3840, 2560], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                        help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    main_photo_xl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_md = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_md2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_sm = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_sm2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    grey_text_photo = models.CharField('Подпись под фото', max_length=500, null=True, blank=True)
    bottom_text_photo = RichTextField('Текст под фото', blank=True, null=True)
    number = models.PositiveIntegerField('Цифра', default=1, blank=True, null=True)
    number_text = models.CharField('Подпись под цифрой', max_length=255, blank=True, null=True)
    title_reward = models.CharField('Заголовок "Награды"', max_length=500, null=True)
    title_create_model = models.CharField('Заголовок "Как мы создаём модели"', max_length=500, null=True)
    video_link = models.CharField('Ссылка на видео Vimeo', max_length=500, blank=True)
    title_press = models.CharField('Заголовок "Мы в прессе"', max_length=500, null=True)
    title_author = models.CharField('Заголовок "Наши авторы"', max_length=500, null=True)

    __original_main_photo_xl2x = None

    def __init__(self, *args, **kwargs):
        super(about_main, self).__init__(*args, **kwargs)
        self.__original_main_photo_xl2x = self.main_photo_xl2x

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.main_photo_xl2x != self.__original_main_photo_xl2x:
            self.main_photo_xl = resize_img(self.main_photo_xl, self.main_photo_xl2x, [1920, 1280])
            self.main_photo_md = resize_img(self.main_photo_md, self.main_photo_xl2x, [1440, 960])
            self.main_photo_md2x = resize_img(self.main_photo_md2x, self.main_photo_xl2x, [2880, 1920])
            self.main_photo_sm = resize_img(self.main_photo_sm, self.main_photo_xl2x, [1280, 853])
            self.main_photo_sm2x = resize_img(self.main_photo_sm2x, self.main_photo_xl2x, [2560, 1707])
            self.main_photo_xs = resize_img(self.main_photo_xs, self.main_photo_xl2x, [768, 512])
            self.main_photo_xs2x = resize_img(self.main_photo_xs2x, self.main_photo_xl2x, [1536, 1024])
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class about_reward(models.Model):
    about = models.ForeignKey(about_main, on_delete=models.CASCADE, related_name='about_rewards', verbose_name='Награды')
    order = models.IntegerField('Порядок показа', null=True)
    title = models.CharField('Заголовок', max_length=255, null=True, blank=True)
    link = models.URLField('Ссылка', null=True, blank=True)
    text = models.CharField('Текст под заголовком', max_length=500, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Награды'
        verbose_name_plural = 'Награды'


class about_press(models.Model):
    about = models.ForeignKey(about_main, on_delete=models.CASCADE, related_name='about_press', verbose_name='Мы в прессе')
    order = models.IntegerField('Порядок показа', null=True)
    main_logo_lg2x = ResizedImageField('Логотип в "Мы в прессе"', size=[256, 256], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                       help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    main_logo_lg = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_logo_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_logo_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    published = models.DateField('Дата публикации')
    title = models.CharField('Заголовок', max_length=255, null=True, blank=True)
    link = models.URLField('Ссылка', null=True, blank=True)

    __original_main_logo_lg2x = None

    def __init__(self, *args, **kwargs):
        super(about_press, self).__init__(*args, **kwargs)
        self.__original_main_logo_lg2x = self.main_logo_lg2x

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.main_logo_lg2x != self.__original_main_logo_lg2x:
            self.main_logo_lg = resize_img(self.main_logo_lg, self.main_logo_lg2x, [128, 128])
            self.main_logo_xs = resize_img(self.main_logo_xs, self.main_logo_lg2x, [80, 80])
            self.main_logo_xs2x = resize_img(self.main_logo_xs2x, self.main_logo_lg2x, [160, 160])
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Мы в прессе'
        verbose_name_plural = 'Мы в прессе'


class about_author(models.Model):
    about = models.ForeignKey(about_main, on_delete=models.CASCADE, related_name='about_authors', verbose_name='Наши авторы')
    order = models.IntegerField('Порядок показа', null=True)
    full_name = models.CharField('Ф.И.О.', max_length=500, null=True)
    author_photo = ResizedImageField('Фото', size=[768, 720], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                       help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    position = models.CharField('Должность', max_length=255, null=True)
    text = RichTextField('Текст', null=True)

    def __str__(self):
        return str(self.full_name)

    class Meta:
        ordering = ['order']
        verbose_name = 'Наши авторы'
        verbose_name_plural = 'Наши авторы'

