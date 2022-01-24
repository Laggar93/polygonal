from django.db import models

# Create your models here.
class map_main(models.Model):
    is_active = models.BooleanField('Активная', default=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Где купить'
        verbose_name_plural = 'Где купить'
