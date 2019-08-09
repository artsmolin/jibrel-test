from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv, find_dotenv
from kombu import Exchange, Queue

load_dotenv(find_dotenv())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jibrel_test.settings')

app = Celery('jibrel_test')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get_daily_rate': {
        'task': 'get_daily_rate',
        'schedule': 60,
    },
}

app.conf.timezone = 'America/Los_Angeles'

app.conf.task_queues = (
    Queue('normal', Exchange('normal'), routing_key='normal'),
)
app.conf.task_default_queue = 'normal'
app.conf.task_default_exchange_type = 'direct'
app.conf.task_default_routing_key = 'normal'

app.conf.task_routes = {
    'handle_report': {
        'queue': 'normal',
        'routing_key': 'agent_reports',
    },
}
