from django.conf.urls import url
from .views import LoginView, LogoutView

app_name = 'auth'

urlpatterns = [
    url(r'^$', LoginView.as_view(), name=''),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
