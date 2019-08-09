from rest_framework.generics import ListAPIView, RetrieveAPIView

from core import models
from core.api.rest import paginations
from . import serializers, authentication


class CurrenciesListView(ListAPIView):
    authentication_classes = [authentication.TestBasicAuthentication]
    queryset = models.Currency.objects.all()
    serializer_class = serializers.CurrencySerializer
    pagination_class = paginations.BasePageNumberPagination


class RateRetrieveView(RetrieveAPIView):
    authentication_classes = [authentication.TestBasicAuthentication]
    queryset = models.Currency.objects.all()
    serializer_class = serializers.CurrencyRateSerializer
