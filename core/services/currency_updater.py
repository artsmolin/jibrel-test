import logging

from django.conf import settings
from django.db import transaction

from core.models import Currency

logger = logging.getLogger(__name__)


class CurrensyUpdater:
    orm_class = Currency

    def update(self):
        logger.info('Initinialization of Currency ...')

        with transaction.atomic():
            for currency_name in settings.CURRENCY_SET:
                self.orm_class.objects.update_or_create(name=currency_name)

    def is_need_to_update(self):
        return (settings.INIT_CURRENCY_ON_APP_START
                and settings.CURRENCY_SET != set(self.orm_class.objects.values_list('name', flat=True)))
