from django.conf.urls import url
from .views import *

app_name = 'note'

urlpatterns = [
    url(r'^view/$', NoteView.as_view(), name='view'),
    url(r'^share/$', NoteShareView.as_view(), name='share'),
]

