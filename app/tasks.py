import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'squadrun.local_settings')

app = Celery('squadrun')
app.config_from_object('django.conf:settings')


@app.task
def adder(x, y):
    return x + y
