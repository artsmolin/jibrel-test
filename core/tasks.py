from core.celery import app
from core.usecases.update_rate import UpdateRate


@app.task(name='get_daily_rate')
def get_daily_rate():
    usecase = UpdateRate()
    usecase.execute()
