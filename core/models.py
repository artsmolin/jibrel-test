from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']


class Rate(models.Model):
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name='rates')
    date = models.BigIntegerField()
    rate = models.IntegerField()
    volume = models.FloatField()

    class Meta:
        ordering = ['date']
