import os
import random
import string
import sys
import uuid
from io import BytesIO

from PIL import Image
from ckeditor.fields import RichTextField
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.html import format_html
from django_resized import ResizedImageField
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


class shop_page(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500)
    all = models.CharField('Заголовок ссылки всех товаров', max_length=200,
                           blank=True)
    no_items = models.CharField('Товары не найдены', max_length=255, blank=True)
    increase = models.CharField('Цена по возрастанию', max_length=255,
                                blank=True)
    decrease = models.CharField('Цена по убыванию', max_length=255, blank=True)
    popular = models.CharField('По популярности', max_length=255, blank=True)
    alphabet = models.CharField('По алфавиту', max_length=255, blank=True)
    difficult = models.CharField('По сложности', max_length=255, blank=True)
    cart = models.CharField('В корзину', max_length=255, blank=True)
    adding_cart = models.CharField('В корзине', max_length=255, blank=True)
    compare = models.CharField('Сравнить', max_length=255, blank=True)
    figure_size = models.CharField('Размер фигуры', max_length=255, blank=True)
    color = models.CharField('Цвет', max_length=255, blank=True)
    complexity = models.CharField('Сложность', max_length=255, blank=True)
    assembly_time = models.CharField('Время сборки', max_length=255, blank=True)
    number = models.CharField('Количество листов', max_length=255, blank=True)
    number_size = models.CharField('Размер листа', max_length=255, blank=True)
    another_items = models.CharField('Этот товар в других форматах', max_length=255, blank=True)
    to_do = models.CharField('Что с этим делать', max_length=255, blank=True)
    megabyte = models.CharField('Мегабайт документа', max_length=255, blank=True)
    delivery = models.CharField('Доставка и оплата', max_length=255, blank=True)
    another_models = models.CharField('Другие модели', max_length=255, blank=True)
    see_more = models.CharField('Подробнее', max_length=255, blank=True)
    page_not_found = models.CharField('Страница не найдена', max_length=255, blank=True)
    new_start = models.CharField('Начать сначала', max_length=255, blank=True)
    of = models.CharField('Из (сложность)', max_length=255, blank=True)
    shop = models.CharField('Магазин', max_length=255, blank=True)
    check_order = models.CharField('Оформить заказ', max_length=255, blank=True)
    more = models.CharField('Больше', max_length=255, blank=True)
    less = models.CharField('Меньше', max_length=255, blank=True)
    total = models.CharField('Итого', max_length=255, blank=True)
    promo_code = models.CharField('Промо-код', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Статический перевод'
        verbose_name_plural = 'Статические переводы'

    def __str__(self):
        return str(self.all)


class category(models.Model):
    order = models.IntegerField('Порядок показа')
    is_active = models.BooleanField('Показывать на сайте', default=True)
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500)
    name = models.CharField('Название', max_length=300)
    slug = models.SlugField('URL', max_length=50, allow_unicode=True, blank=True,
                            help_text='URL генерируется автоматически из названия раздела, но может быть задан вручную', unique=True)
    figure_size_heading = models.CharField('Заголовок размера фигуры', default='Размер фигуры', max_length=300)
    paper_size_heading = models.CharField('Заголовок размера бумаги', default='Размер бумаги', max_length=300)
    color_heading = models.CharField('Заголовок цвета', default='Цвет', max_length=300)
    difficulty_heading = models.CharField('Заголовок сложности', default='Сложность', max_length=300)
    time_heading = models.CharField('Заголовок времени сбора', default='Время сбора', max_length=300)
    paper_amount_heading = models.CharField('Заголовок количество листов', default='Количество листов', max_length=300)
    connected_items_heading = models.CharField('Заголовок товара в других категориях', default='Товар в других категориях', max_length=300)
    bottom_heading = models.CharField('Заголовок нижнего блока', default='Что с этим делать', max_length=300)
    delivery_heading = models.CharField('Заголовок доставки и оплаты', default='Доставка и оплата', max_length=300)
    other_models_heading = models.CharField('Заголовок других моделей', default='Другие модели', max_length=300)
    index_photo_xs2x = ResizedImageField('Картинка на главной странице', size=[2048, 1410], crop=['middle', 'center'], null=True, upload_to=get_file_path, quality=80,
                                        help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    index_photo_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    index_photo_lg = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    index_photo_lg2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    index_photo_sm = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    index_photo_sm2x = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    index_text = models.TextField('Текст на главной странице', blank=True, null=True)

    __original_index_photo_xs2x = None

    def __init__(self, *args, **kwargs):
        super(category, self).__init__(*args, **kwargs)
        self.__original_index_photo_xs2x = self.index_photo_xs2x

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = 'материал'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.index_photo_xs2x != self.__original_index_photo_xs2x:
            self.index_photo_xs = resize_img(self.index_photo_xs, self.index_photo_xs2x, [1024, 705])
            self.index_photo_lg = resize_img(self.index_photo_lg, self.index_photo_xs2x, [480, 330])
            self.index_photo_lg2x = resize_img(self.index_photo_lg2x, self.index_photo_xs2x, [960, 661])
            self.index_photo_sm = resize_img(self.index_photo_sm, self.index_photo_xs2x, [768, 529])
            self.index_photo_sm2x = resize_img(self.index_photo_sm2x, self.index_photo_xs2x, [1536, 1058])

        if not self.slug:
            self.slug = slugify(self.name)[:50]
        else:
            self.slug = slugify(self.slug)[:50]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_view', kwargs={'category_slug': self.slug})


class subcategory(models.Model):
    order = models.IntegerField('Порядок показа')
    is_active = models.BooleanField('Показывать на сайте', default=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, verbose_name='Категория', related_name='in_category')
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500)
    name = models.CharField('Название', max_length=300)
    slug = models.SlugField('URL', max_length=50, allow_unicode=True, blank=True,
                            help_text='URL генерируется автоматически из названия раздела, но может быть задан вручную')

    def __str__(self):
        return str(self.category) + ' — ' + self.name

    class Meta:
        ordering = ['order']
        verbose_name = 'материал'
        verbose_name_plural = 'Подкатегории'
        unique_together = ['category', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        else:
            self.slug = slugify(self.slug)[:50]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('subcategory_view', kwargs={'category_slug': self.category.slug, 'subcategory_slug': self.slug})


class item(models.Model):
    order = models.IntegerField('Порядок показа')
    views = models.IntegerField('Количество просмотров товара', null=True, blank=True, default=0)
    is_active = models.BooleanField('Показывать на сайте', default=True)
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500)
    slug = models.SlugField('URL', max_length=50, allow_unicode=True, blank=True,
                            help_text='URL генерируется автоматически из названия раздела, но может быть задан вручную', unique=True)
    name = models.CharField('Название', max_length=500)
    name_lower = models.CharField('Название в нижнем регистре', max_length=500, null=True)
    category = models.ForeignKey(subcategory, on_delete=models.CASCADE, verbose_name='Категория')
    main_photo_xxl2 = ResizedImageField('Основное изображение', size=[2400, 1800], crop=['middle', 'center'], upload_to=get_file_path, quality=80,
                                        help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.')
    main_photo_popup = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs2 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_thumb_xs2 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_thumb_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    video_title = models.CharField('Заголовок видео-ссылки под слайдером', max_length=500, blank=True)
    video_link = models.CharField('Ссылка на видео под слайдером', max_length=500, blank=True)
    figure_size = models.CharField('Размеры фигуры', max_length=100, blank=True)
    paper_size = models.CharField('Размеры листа', max_length=100, blank=True)
    color = models.CharField('Цвет', max_length=500, blank=True)
    difficulty = models.CharField('Сложность',
                                  choices=[('1', 'Низкая'), ('2', 'Средняя'),
                                           ('3', 'Высокая')], max_length=100, blank=True)
    time = models.CharField('Время сборки', max_length=500, blank=True)
    paper_amount = models.CharField('Количество листов', max_length=500, blank=True)
    about = RichTextField('Текст справа', blank=True)
    connected_items = models.ManyToManyField('self', blank=True, verbose_name='Связанные товары')
    bottom_photo_xxl2 = ResizedImageField('Картинка для нижнего блока', size=[3200, 2400], crop=['middle', 'center'],
                                          upload_to=get_file_path, quality=80,
                                          help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.', blank=True)
    bottom_photo_xs2 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    bottom_photo_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    bottom_photo_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    bottom_list = RichTextField('Список для нижнего блока', blank=True)
    bottom_link_title = models.CharField('Заголовок файла для нижнего блока', max_length=500, blank=True)
    bottom_link = models.FileField('Файл для нижнего блока', upload_to=get_file_path, validators=[FileExtensionValidator(['pdf'])],
                                   help_text='Формат файла: pdf. Ограничени размера: 1 Мбайт.', blank=True)
    bottom_text = RichTextField('Текст под нижним блоком', blank=True)
    price_rub = models.FloatField('Цена в рублях', null=True, blank=True)
    price_eur = models.FloatField('Цена в евро', null=True, blank=True)
    price_usd = models.FloatField('Цена в долларах', null=True, blank=True)
    weight = models.FloatField('Вес товара, кг', null=True, blank=True)
    length = models.FloatField('Длина, мм', null=True, blank=True)
    width = models.FloatField('Ширина, мм', null=True, blank=True)
    height = models.FloatField('Высота, мм', null=True, blank=True)
    __original_main_photo_xxl2 = None
    __original_bottom_photo_xxl2 = None

    def __init__(self, *args, **kwargs):
        super(item, self).__init__(*args, **kwargs)
        self.__original_main_photo_xxl2 = self.main_photo_xxl2
        self.__original_bottom_photo_xxl2 = self.bottom_photo_xxl2

    def get_absolute_url(self):
        return reverse('catalog_item', kwargs={'category_slug': self.category.category.slug,
                                               'subcategory_slug': self.category.slug, 'item_slug': self.slug})

    def __str__(self):
        return str(self.category) + ': ' + str(self.name)

    class Meta:
        ordering = ['order']
        verbose_name = 'материал'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.main_photo_xxl2 != self.__original_main_photo_xxl2:
            self.main_photo_popup = resize_img(self.main_photo_popup, self.main_photo_xxl2, [1600, 1200])
            self.main_photo_xs2 = resize_img(self.main_photo_xs2, self.main_photo_xxl2, [1536, 1152])
            self.main_photo_xxl = resize_img(self.main_photo_xxl, self.main_photo_xxl2, [1200, 900])
            self.main_photo_xs = resize_img(self.main_photo_xs, self.main_photo_xxl2, [768, 576])
            self.main_photo_thumb_xs2 = resize_img(self.main_photo_thumb_xs2, self.main_photo_xxl2, [288, 288])
            self.main_photo_thumb_xs = resize_img(self.main_photo_thumb_xs, self.main_photo_xxl2, [144, 144])
        if self.bottom_photo_xxl2 != self.__original_bottom_photo_xxl2:
            self.bottom_photo_xs2 = resize_img(self.bottom_photo_xs2, self.bottom_photo_xxl2, [1536, 1152])
            self.bottom_photo_xxl = resize_img(self.bottom_photo_xxl, self.bottom_photo_xxl2,[1200, 900])
            self.bottom_photo_xs = resize_img(self.bottom_photo_xs, self.bottom_photo_xxl2, [768, 576])
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        else:
            self.slug = slugify(self.slug)[:50]

        self.name_lower = self.name.lower()
        super().save(*args, **kwargs)

    @cached_property
    def display_main_image(self):
        return format_html('<img src="{img}" width="300">', img=self.main_photo_xxl2.url)

    display_main_image.short_description = 'Предпросмотр основного изображения'

    def display_bottom_image(self):
        return format_html('<img src="{img}" width="300">', img=self.bottom_photo_xxl2.url)

    display_bottom_image.short_description = 'Предпросмотр изображения нижнего блока'


class item_photos(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    order = models.IntegerField('Порядок показа')
    main_photo_xxl2 = ResizedImageField('Картинка', size=[3200, 2400], crop=['middle', 'center'], upload_to=get_file_path, quality=80,
                                        help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.')
    main_photo_popup = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs2 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xxl = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_thumb_xs2 = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    main_photo_thumb_xs = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    __original_main_photo_xxl2 = None

    def __init__(self, *args, **kwargs):
        super(item_photos, self).__init__(*args, **kwargs)
        self.__original_main_photo_xxl2 = self.main_photo_xxl2

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['order']
        verbose_name = 'материал'
        verbose_name_plural = 'Изображения для слайдера'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.main_photo_xxl2 != self.__original_main_photo_xxl2:
            self.main_photo_popup = resize_img(self.main_photo_popup, self.main_photo_xxl2, [1600, 1200])
            self.main_photo_xs2 = resize_img(self.main_photo_xs2, self.main_photo_xxl2, [1536, 1152])
            self.main_photo_xxl = resize_img(self.main_photo_xxl, self.main_photo_xxl2, [1200, 900])
            self.main_photo_xs = resize_img(self.main_photo_xs, self.main_photo_xxl2, [768, 576])
            self.main_photo_thumb_xs2 = resize_img(self.main_photo_thumb_xs2, self.main_photo_xxl2, [288, 288])
            self.main_photo_thumb_xs = resize_img(self.main_photo_thumb_xs, self.main_photo_xxl2, [144, 144])
        super().save(*args, **kwargs)

    @cached_property
    def display_image(self):
        return format_html('<img src="{img}" width="300">', img=self.main_photo_xxl2.url)

    display_image.short_description = 'Предпросмотр'


class item_terms(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    order = models.IntegerField('Порядок показа')
    text = models.TextField('Текст пункта')

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['order']
        verbose_name = 'материал'
        verbose_name_plural = 'Доставка и оплата'


class item_files(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    order = models.IntegerField('Порядок показа')
    file = models.FileField('Файл', upload_to=get_file_path, validators=[FileExtensionValidator(['jpg', 'zip', 'pdf'])],
                            help_text='Формат файла: jpg, zip или pdf. Ограничени размера: 3 Мбайт.')

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['order']
        verbose_name = 'материал'
        verbose_name_plural = 'Схемы для отправки на почту'


class discount(models.Model):
    item = models.ManyToManyField(item, blank=True, verbose_name="Товары")
    is_active = models.BooleanField('Активная', default=True)
    name = models.CharField('Название скидки', max_length=500)
    type = models.CharField('Тип', choices=[('1', 'Процент'), ('2', 'Валюта')], max_length=100, blank=True)
    amount_ru = models.FloatField('Величина скидки рубля', blank=True, null=True)
    amount_usd = models.FloatField('Величина скидки доллара', blank=True, null=True)
    amount_eur = models.FloatField('Величина скидки евро', blank=True, null=True)
    starts = models.DateField('Начало действия', blank=True, null=True)
    ends = models.DateField('Окончание действия', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'Скидки'

    def get_currency_price(self):
        item = self.item.first()
        right_now = timezone.now().date()
        if self.starts <= right_now <= self.ends:
            results = [None, None, None]
            if self.type == '2':
                if item.price_rub:
                    item.price_rub = item.price_rub - self.amount_ru
                    results[0] = item.price_rub
                if item.price_usd:
                    item.price_usd = item.price_usd - self.amount_usd
                    results[1] = item.price_usd
                if item.price_eur:
                    item.price_eur = item.price_eur - self.amount_eur
                    results[2] = item.price_eur
                return results

            if self.type == '1':
                if item.price_rub:
                    item.price_rub = item.price_rub - ((item.price_rub / 100) * self.amount_ru)
                    results[0] = item.price_rub
                if item.price_usd:
                    item.price_usd = item.price_usd - ((item.price_usd / 100) * self.amount_usd)
                    results[1] = item.price_usd
                if item.price_eur:
                    item.price_eur = item.price_eur - ((item.price_eur / 100) * self.amount_eur)
                    results[2] = item.price_eur
                return results
        else:
            if item.price_rub:
                item.price_rub = item.price_rub
            if item.price_usd:
                item.price_usd = item.price_usd
            if item.price_eur:
                item.price_eur = item.price_eur


class coupon(models.Model):
    item = models.ManyToManyField(item, blank=True, verbose_name="Товары")
    is_active = models.BooleanField('Активная', default=True)
    name = models.CharField('Название купона', max_length=500)
    number = models.CharField('Номер купона (генерируется автоматически)', max_length=500, blank=True)
    usage = models.CharField('Возможность использования', choices=[('1', 'Одноразовый'), ('2', 'Многоразовый')],
                             max_length=100, blank=True)
    type = models.CharField('Тип', choices=[('1', 'Процент'), ('2', 'Валюта')], max_length=100, blank=True)
    amount = models.FloatField('Величина купона', blank=True, null=True)
    starts = models.DateTimeField('Начало действия', blank=True, null=True)
    ends = models.DateTimeField('Окончание действия', blank=True, null=True)
    used = models.BooleanField('Использован', default=False, blank=True)

    def save(self, *args, **kwargs):
        if self.number == '':
            self.number = ''.join(
                random.choice(string.ascii_uppercase + string.digits) for _ in
                range(10))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'Купоны'


class item_basket(models.Model):
    session_key = models.CharField('Ключ сессии', max_length=500, blank=True)
    item = models.ForeignKey(item, on_delete=models.CASCADE, verbose_name='Товар')
    amount = models.IntegerField('Количество', null=True)

    def __str__(self):
        return self.session_key

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'Список заказов'
