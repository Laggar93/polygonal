import os
import sys
import uuid
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import FileExtensionValidator
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


class index_main(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500, blank=True)
    title_page = models.CharField('Заголовок страницы', max_length=500, blank=True)
    title_text = models.CharField('Текст под заголовком', max_length=500, blank=True)
    main_photo_xl2x = ResizedImageField('Картинка', size=[3840, 1720], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                        help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    main_photo_xl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_md = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_md2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_sm = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_sm2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    first_figure_sticker_xs2 = ResizedImageField('Картинка первой фигуры', size=[640, 1080], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                                 help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    first_figure_sticker_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    first_figure_button_name = models.CharField('Название кнопки первой фигуры', max_length=500, blank=True)
    first_figure_button_link = models.CharField('Ссылка кнопки первой фигуры', max_length=500, blank=True)
    second_figure_sticker_xs2 = ResizedImageField('Картинка второй фигуры', size=[600, 788], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                                  help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    second_figure_sticker_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    second_figure_button_name = models.CharField('Название кнопки второй фигуры', max_length=500, blank=True)
    second_figure_button_link = models.CharField('Ссылка кнопки второй фигуры', max_length=500, blank=True)
    figure_title = models.CharField('Заголовок между фигурами', max_length=500, blank=True)
    figure_text = models.TextField('Текст между фигурами', blank=True, null=True)
    proud_title = models.CharField('Заголовок "Мы гордимся"', max_length=500, blank=True, null=True)
    proud_text = models.TextField('Текст под заголовком "Мы гордимся"', blank=True, null=True)
    model_file = models.FileField('Файл модели', upload_to=get_file_path, validators=[FileExtensionValidator(['pdf', 'zip', 'gz'])],
                                  help_text='Формат файла: pdf. Ограничение размера: 1 Мбайт.', blank=True)
    title_link = models.CharField('Заголовок ссылки скачивания', max_length=500, blank=True, null=True)
    proud_picture_xs2 = ResizedImageField('Картинка "Мы гордимся"', size=[992, 658], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                                 help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    proud_picture_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    third_figure_sticker_xs2 = ResizedImageField('Картинка третьей фигуры', size=[640, 758], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                                 help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    third_figure_sticker_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    third_figure_button_name = models.CharField('Название кнопки третьей фигуры', max_length=500, blank=True)
    third_figure_button_link = models.CharField('Ссылка кнопки третьей фигуры', max_length=500, blank=True)
    fourth_figure_sticker_xs2 = ResizedImageField('Картинка четвертой фигуры', size=[600, 801], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                                  help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    fourth_figure_sticker_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    fourth_figure_button_name = models.CharField('Название кнопки четвертой фигуры', max_length=500, blank=True)
    fourth_figure_button_link = models.CharField('Ссылка кнопки четвертой фигуры', max_length=500, blank=True)

    __original_main_photo_xl2x = None
    __original_first_figure_sticker_xs2 = None
    __original_second_figure_sticker_xs2 = None
    __original_third_figure_sticker_xs2 = None
    __original_fourth_figure_sticker_xs2 = None
    __original_proud_picture_xs2 = None

    def __init__(self, *args, **kwargs):
        super(index_main, self).__init__(*args, **kwargs)
        self.__original_main_photo_xl2x = self.main_photo_xl2x
        self.__original_first_figure_sticker_xs2 = self.first_figure_sticker_xs2
        self.__original_second_figure_sticker_xs2 = self.second_figure_sticker_xs2
        self.__original_third_figure_sticker_xs2 = self.third_figure_sticker_xs2
        self.__original_fourth_figure_sticker_xs2 = self.fourth_figure_sticker_xs2
        self.__original_proud_picture_xs2 = self.proud_picture_xs2

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.main_photo_xl2x != self.__original_main_photo_xl2x:
            self.main_photo_md2x = resize_img(self.main_photo_md2x, self.main_photo_xl2x, [2880, 1290])
            self.main_photo_sm2x = resize_img(self.main_photo_sm2x, self.main_photo_xl2x, [2560, 1147])
            self.main_photo_xl = resize_img(self.main_photo_xl, self.main_photo_xl2x, [1920, 860])
            self.main_photo_xs2x = resize_img(self.main_photo_xs2x, self.main_photo_xl2x, [1536, 688])
            self.main_photo_md = resize_img(self.main_photo_md, self.main_photo_xl2x, [1440, 645])
            self.main_photo_sm = resize_img(self.main_photo_sm, self.main_photo_xl2x, [1280, 573])
            self.main_photo_xs = resize_img(self.main_photo_xs, self.main_photo_xl2x, [768, 344])
        if self.first_figure_sticker_xs2 != self.__original_first_figure_sticker_xs2:
            self.first_figure_sticker_xs = resize_img(self.first_figure_sticker_xs, self.first_figure_sticker_xs2, [320, 540])
        if self.second_figure_sticker_xs2 != self.__original_second_figure_sticker_xs2:
            self.second_figure_sticker_xs = resize_img(self.second_figure_sticker_xs, self.second_figure_sticker_xs2, [300, 394])
        if self.third_figure_sticker_xs2 != self.__original_third_figure_sticker_xs2:
            self.third_figure_sticker_xs = resize_img(self.third_figure_sticker_xs, self.third_figure_sticker_xs2, [320, 379])
        if self.fourth_figure_sticker_xs2 != self.__original_fourth_figure_sticker_xs2:
            self.fourth_figure_sticker_xs = resize_img(self.fourth_figure_sticker_xs, self.fourth_figure_sticker_xs2, [300, 400])
        if self.proud_picture_xs2 != self.__original_proud_picture_xs2:
            self.proud_picture_xs = resize_img(self.proud_picture_xs, self.proud_picture_xs2, [496, 329])
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title_page)

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class order_point(models.Model):
    index = models.ForeignKey(index_main, verbose_name='Пункты списка', on_delete=models.CASCADE, related_name='points')
    order = models.IntegerField('Порядок показа')
    point = models.TextField('Пункты списка проекта на заказ', blank=True, null=True)

    def __str__(self):
        return str(self.point)

    class Meta:
        ordering = ['order']
        verbose_name = 'Пункты списка'
        verbose_name_plural = 'Пункты списка'


class index_translate(models.Model):
    catalog = models.CharField('Смотреть каталог', max_length=255, blank=True, null=True)
    shop = models.CharField('Перейти в магазин', max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.catalog)

    class Meta:
        verbose_name = 'Переводы на главной странице'
        verbose_name_plural = 'Переводы на главной странице'