from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment

from TecNotesPlus.settings import STATIC_URL


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'BASE_TEMPLATE': 'core/base.html',
        'STATIC_URL': STATIC_URL,
    })
    return env
