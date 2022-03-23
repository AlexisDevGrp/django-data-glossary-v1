from __future__ import absolute_import

import os

from celery import Celery
from datagloss.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datagloss.settings.development")

app = Celery("datagloss")

app.config_from_object("datagloss.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
