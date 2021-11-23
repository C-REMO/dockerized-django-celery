import os
from celery import Celery
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.common')
app = Celery('settings')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    "execute-every-30-seconds": {
        "task": "symbols.tasks.task_save_yahoo_feeds",
        "schedule": timedelta(seconds=30),
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
