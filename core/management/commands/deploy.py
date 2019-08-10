from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import Currency


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with transaction.atomic():
            for currency_name in settings.CURRENCY_SET:
                Currency.objects.update_or_create(name=currency_name)
