from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter



from TecNotesPlus import settings
from .views import *

app_name = 'announcement'

router = DefaultRouter()
router.register('api', NoteViewSet, basename='api')

urlpatterns = [
    url(r'^view/$', NoteView.as_view(), name='view'),

    url(r'^', include(router.urls)),
]

