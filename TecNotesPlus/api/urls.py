from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from TecNotesPlus.auth.views import login_user, LogoutView
from note.views import *

app_name = 'api'

router = DefaultRouter()
router.register('note', NoteViewSet, basename='note')
router.register('note_share', NoteShareViewSet, basename='note_share')

urlpatterns = [
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^', include(router.urls)),
]
