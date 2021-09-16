from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from TecNotesPlus.auth import jwt_customized_views
from rest_framework_simplejwt import views as jwt_views

from TecNotesPlus.auth.views import *
from note.views import *

app_name = 'api'

router = DefaultRouter()
router.register('note', NoteViewSet, basename='note')
router.register('note_share', NoteShareViewSet, basename='note_share')

urlpatterns = [
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^change_password/', ChangePasswordView.as_view(),
        name='change_password'),

    url(r'token/$', jwt_customized_views.CustomTokenObtainPairView.as_view(), name='token'),
    url(r'token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    url(r'^update_status/$', update_note_share_status, name='update_status'),
    url(r'^', include(router.urls)),

]
