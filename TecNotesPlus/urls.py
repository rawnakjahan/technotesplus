"""TecNotesPlus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.urls import path


from TecNotesPlus import settings
from TecNotesPlus.auth.views import LoginView
from note.views import NoteViewSet


def go_to(self):
    return redirect(settings.LOGIN_URL)

urlpatterns = [
    url(r'^$', go_to),

    url(r'^api/', include('TecNotesPlus.api.urls', 'api')),
    url(r'^login/', include('TecNotesPlus.auth.urls', 'login')),
    url(r'^note/', include('note.urls', 'note')),

    # url(r'^note/', include('note.urls', 'note')),

    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
                                       document_root=settings.STATIC_ROOT,
                                       show_indexes=True)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                                       document_root=settings.MEDIA_ROOT,
                                       show_indexes=True)

    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
