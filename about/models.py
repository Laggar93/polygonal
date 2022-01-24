from django.db import models

# Create your models here.
class about_main(models.Model):
    name = models.CharField('Название в меню', max_length=255, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'