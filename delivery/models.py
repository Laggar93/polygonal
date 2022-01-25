from ckeditor.fields import RichTextField
from django.db import models


class delivery_main(models.Model):
    keywords = models.CharField('Ключевые слова', max_length=1000, blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    title = models.CharField('Заголовок', max_length=500)
    delivery = models.CharField('Доставка и оплата', max_length=255, blank=True)
    name = models.CharField('Название раздела', max_length=500)
    payment = models.CharField('Оплата', max_length=500)
    top_text = RichTextField('Вступительный текст', blank=True, null=True)
    bottom_text = RichTextField('Нижний текст', blank=True, null=True)
    paypal_logo = models.BooleanField('PayPal', default=True)
    visa_logo = models.BooleanField('Visa', default=True)
    master_logo = models.BooleanField('Master Card', default=True)
    mir_logo = models.BooleanField('МИР', default=True)
    terminal_logo = models.BooleanField('Terminal', default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Доставка и оплата'
        verbose_name_plural = 'Доставка и оплата'


class delivery_article(models.Model):
    order = models.IntegerField('Порядок показа', null=True)
    title = models.CharField('Заголовок', max_length=500)
    intro_text = RichTextField('Вступительный текст', blank=True, null=True)
    country = models.CharField('Страна', max_length=255, blank=True)
    bold_text = RichTextField('Жирный текст под таблицей', blank=True, null=True)
    grey_text = RichTextField('Серый текст под таблицей', blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['order']
        verbose_name = 'Список статей доставки и оплаты'
        verbose_name_plural = 'Списки статей доставки и оплаты'

class delivery_columns(models.Model):
    order = models.IntegerField('Порядок показа', null=True)
    delivery_article = models.ForeignKey(delivery_article, related_name='article_columns', on_delete=models.CASCADE, verbose_name='Списки статей доставки и оплаты')
    first_column = models.CharField('Первый столбец', max_length=500, blank=True, null=True)
    second_column = models.CharField('Второй столбец', max_length=500, blank=True, null=True)
    third_column = models.CharField('Третий столбец', max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Столбец'
        verbose_name_plural = 'Столбцы'







