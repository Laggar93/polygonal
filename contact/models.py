import os
import sys
import uuid
from io import BytesIO

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


class contact_main(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500, blank=True)
    name = models.CharField('Название раздела в меню', max_length=500, blank=True)
    intro_title = models.CharField('Приходите в гости', max_length=500, blank=True)
    address = models.CharField('Адрес', max_length=500, blank=True, null=True)
    map_link = models.CharField('Ссылка на карту', max_length=500, blank=True, null=True)
    work_mode = models.CharField('Режим работы', max_length=500, blank=True, null=True)
    first_phone = models.CharField('Первый телефон', max_length=255, blank=True, null=True)
    second_phone = models.CharField('Второй телефон', max_length=255, blank=True, null=True)
    email = models.CharField('Почта', blank=True, max_length=255, null=True)

    main_photo_xl2x = ResizedImageField('Картинка в "контактах"', size=[3840, 1456], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                        help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    main_photo_xl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_md = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_md2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_sm = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_sm2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xl1 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xl12x = models.ImageField(upload_to=get_file_path, blank=True, null=True)

    __original_main_photo_xl2x = None

    def __init__(self, *args, **kwargs):
        super(contact_main, self).__init__(*args, **kwargs)
        self.__original_main_photo_xl2x = self.main_photo_xl2x

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.main_photo_xl2x != self.__original_main_photo_xl2x:
            self.main_photo_xl = resize_img(self.main_photo_xl, self.main_photo_xl2x, [1900, 728])
            self.main_photo_md = resize_img(self.main_photo_md, self.main_photo_xl2x, [1440, 546])
            self.main_photo_md2x = resize_img(self.main_photo_md2x, self.main_photo_xl2x, [2880, 1092])
            self.main_photo_sm = resize_img(self.main_photo_sm, self.main_photo_xl2x, [1280, 485])
            self.main_photo_sm2x = resize_img(self.main_photo_sm2x, self.main_photo_xl2x, [2560, 971])
            self.main_photo_xs = resize_img(self.main_photo_xs, self.main_photo_xl2x, [768, 291])
            self.main_photo_xs2x = resize_img(self.main_photo_xs2x, self.main_photo_xl2x, [1536, 582])
            self.main_photo_xl1 = resize_img(self.main_photo_xl1, self.main_photo_xl2x, [1920, 728])
            self.main_photo_xl12x = resize_img(self.main_photo_xl12x, self.main_photo_xl2x, [3840, 1456])
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.address)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class contact_social_networks(models.Model):
    contact = models.ForeignKey(contact_main, on_delete=models.CASCADE, verbose_name='Контакты', related_name='contact_networks')
    order = models.IntegerField('Порядок показа', null=True)
    social_network_url = models.URLField('Ссылка на социальную сеть')
    social_network_type = models.CharField('Тип социальной сети', choices=[('1', 'WhatsApp'), ('2', 'Telegram'), ('3', 'Behance'),
                                                                           ('4', 'Facebook'), ('5', 'В Контакте'),
                                                                           ('6', 'Instagram'), ('7', 'YouTube')], max_length=100, unique=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        ordering = ['order']
        verbose_name = 'Соц. сети в контактах'
        verbose_name_plural = 'Соц. сети в контактах'


class contact_form(models.Model):
    heading = models.CharField('Заголовок формы', max_length=500, blank=True)
    name = models.CharField('Заголовок поля ФИО', max_length=500, blank=True)
    email = models.CharField('Заголовок поля электронная почта', max_length=500, blank=True)
    number = models.CharField('Заголовок поля телефон', max_length=500, blank=True)
    message = models.TextField('Заголовок поля сообщение', max_length=500, blank=True)
    send = models.CharField('Заголовок кнопки', max_length=500, blank=True)
    success = models.CharField('Успешная отправка', max_length=500, blank=True)
    error = models.CharField('Неуспешная отправка', max_length=500, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Письмо нам'
        verbose_name_plural = 'Письмо нам'
