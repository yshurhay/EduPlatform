from django.db import models


class Specialization(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Специализации"
        verbose_name_plural = "Специализации"
        ordering = ['id']

    def __str__(self):
        return f'Specialization #{self.pk} - {self.title}'
