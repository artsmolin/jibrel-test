from django.db.models import Avg
from rest_framework import serializers

from core import models


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = ['id', 'name']


class CurrencyRateSerializer(serializers.ModelSerializer):
    last_rate = serializers.SerializerMethodField()
    volume_avg = serializers.SerializerMethodField()

    class Meta:
        model = models.Currency
        fields = '__all__'

    @staticmethod
    def get_last_rate(instance):
        return instance.rates.last().rate

    @staticmethod
    def get_volume_avg(instance):
        return instance.rates.aggregate(Avg('volume'))['volume__avg']
