from django.contrib.auth.models import User
from django.db import models


class NOTE(models.Model):
    title = models.TextField(max_length=512, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


