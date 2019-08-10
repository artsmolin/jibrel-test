import logging
from datetime import datetime

from core.constants import currensy_to_bitfinex_symbol_mapping
from core.external_api import bitfinex_api
from core.models import Currency, Rate


logger = logging.getLogger(__name__)


class UpdateRate:
    def execute(self):
        days_10_ts = 864000000  # ms
        now_ts = datetime.utcnow().timestamp() * 1000
        days_10_ago_ts = now_ts - days_10_ts

        for currency in Currency.objects.all():
            last_rate = Rate.objects.only('date').filter(currency_id=currency.id).last()

            # Загружаем все недостающие данные либо с момента "10 дней назад",
            # либо с момента "последний сохранённый курс",
            # в зависимости от того, какой момент ближе к текущей временной точке.
            after = max(days_10_ago_ts, last_rate.date if last_rate else 0)
            candles = self.obtain_all(currensy_to_bitfinex_symbol_mapping[currency.name], '1m', after=after)

            logger.info(f'obtained for {currency.name}: {len(candles)}')

            Rate.objects.bulk_create([Rate(
                rate=candle.close,
                volume=candle.volume,
                date=candle.mts,
                currency_id=currency.id,
            ) for candle in candles])

            # Объём данных небольшой, можем позволить себе удалять прямо в этой таске.
            Rate.objects.filter(currency_id=currency.id, date__lt=days_10_ago_ts).delete()

    @staticmethod
    def obtain_all(symbol, time_frame, section='hist', after=None):
        # Загружаем курсы до тех пор, пока есть что грузить (лимит на 1 запрос - 5000 записей)
        all_obtained = False
        result = []

        while not all_obtained:
            if result:
                after = result[0].mts

            candles = bitfinex_api.get_candles(symbol, time_frame, section, after=after)
            if not candles:
                all_obtained = True

            result = candles + result

        return result
