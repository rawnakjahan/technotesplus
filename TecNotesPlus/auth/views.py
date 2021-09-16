from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from rest_framework.decorators import api_view
from rest_framework.response import Response

from TecNotesPlus.settings import LOGIN_URL

from rest_framework import serializers, viewsets, mixins, status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.db import transaction
from rest_framework import exceptions

# render application authentication page


def time_difference(time_from, time_to):
    diff = time_from - time_to
    seconds = diff.seconds
    minutes = seconds / 60
    return minutes


def login_attempt(username, attempt):
    users = User.objects.filter(username=username)
    if users:
        user = users[0]

        if attempt == 'success':
            if user.is_locked:
                minutes = time_difference(timezone.now(), user.locked_at)
                if minutes <= settings.LOCKED_TIME:
                    raise exceptions.AuthenticationFailed(
                        'Your account is Locked due to Unsuccessful login attempts. Try again after {} minute'.format(
                            round(settings.LOCKED_TIME - minutes, 2)))
            user.is_locked = False
            user.unsuccessful_attempt = 0
            password_updated_at = user.password_updated_at
            if password_updated_at:
                days = timezone.now() - password_updated_at
                if int(days.days) > settings.PASSWORD_MAX_DAY:
                    user.need_change_pass = True
                else:
                    user.need_change_pass = False
            user.save()
        else:
            if user.role.id != 1:
                unsuccessful_attempt = user.unsuccessful_attempt + 1
                user.unsuccessful_attempt = unsuccessful_attempt
                user.save()
                if unsuccessful_attempt > settings.UNSUCCESSFUL_ATTEMPT:
                    user.is_locked = True
                    user.locked_at = timezone.now()
                    user.save()
            if user.is_locked:
                minutes = time_difference(timezone.now(), user.locked_at)
                if minutes <= settings.LOCKED_TIME:
                    raise exceptions.AuthenticationFailed(
                        'Your account is Locked due to Unsuccessful login attempts. Try again after {} minute'.format(
                            round(settings.LOCKED_TIME - minutes, 2)))


class LoginView(TemplateView):
    template_name = 'core/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            next_url = request.GET.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)

            return redirect('note:view')
        return render(request, template_name=self.template_name)


# logout a user
class LogoutView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user.id
            logout(request)

        return redirect(LOGIN_URL)


class LoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': ''}),
        error_messages={'required': 'Username/Email can not be empty.'}
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
        error_messages={'required': 'Password can not be empty.'}
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive. Please contact with administrator."),
        'expired': _("Your account has been expired. Please contact with administrator. 'Thank you"),
    }

    def confirm_login_allowed(self, user):
        print("confirm_login_allowed")


@api_view(['POST'])
def login_user(request):
    username = request.POST['username']
    form = LoginForm(request, data=request.POST)

    if form.is_valid():
        login(request, user=form.get_user())
        return Response(status=200)
    else:
        message = ''
        for error in form.errors:
            message += "%s" % (form.errors[error])
        return Response({'detail': message}, status=400)


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
