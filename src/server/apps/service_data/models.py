from django.db import models


class UserWeight(models.Model):

    user_id = models.CharField(
        max_length=255,
    )

    day = models.DateField()

    weight = models.FloatField()

    class Meta:
        verbose_name = 'weight'
        verbose_name_plural = 'weights'

