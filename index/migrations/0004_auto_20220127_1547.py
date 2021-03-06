# Generated by Django 3.2.4 on 2022-01-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20220127_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_main',
            name='description_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='description_fr',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='description_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='figure_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Текст между фигурами'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='figure_text_fr',
            field=models.TextField(blank=True, null=True, verbose_name='Текст между фигурами'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='figure_text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Текст между фигурами'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='figure_title_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок между фигурами'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='figure_title_fr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок между фигурами'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='figure_title_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок между фигурами'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='first_figure_button_name_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки первой фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='first_figure_button_name_fr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки первой фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='first_figure_button_name_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки первой фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='fourth_figure_button_name_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки четвертой фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='fourth_figure_button_name_fr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки четвертой фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='fourth_figure_button_name_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки четвертой фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='keywords_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='keywords_fr',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='keywords_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='proud_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Текст под заголовком "Мы гордимся"'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='proud_text_fr',
            field=models.TextField(blank=True, null=True, verbose_name='Текст под заголовком "Мы гордимся"'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='proud_text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Текст под заголовком "Мы гордимся"'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='proud_title_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок "Мы гордимся"'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='proud_title_fr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок "Мы гордимся"'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='proud_title_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок "Мы гордимся"'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='second_figure_button_name_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки второй фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='second_figure_button_name_fr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки второй фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='second_figure_button_name_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки второй фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='third_figure_button_name_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки третьей фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='third_figure_button_name_fr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки третьей фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='third_figure_button_name_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название кнопки третьей фигуры'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_fr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_link_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок ссылки скачивания'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_link_fr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок ссылки скачивания'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_link_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок ссылки скачивания'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_page_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_page_fr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_page_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_text_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Приходите в гости'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_text_fr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Приходите в гости'),
        ),
        migrations.AddField(
            model_name='index_main',
            name='title_text_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Приходите в гости'),
        ),
        migrations.AddField(
            model_name='order_point',
            name='point_en',
            field=models.TextField(blank=True, null=True, verbose_name='Пункты списка проекта на заказ'),
        ),
        migrations.AddField(
            model_name='order_point',
            name='point_fr',
            field=models.TextField(blank=True, null=True, verbose_name='Пункты списка проекта на заказ'),
        ),
        migrations.AddField(
            model_name='order_point',
            name='point_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Пункты списка проекта на заказ'),
        ),
    ]
