from django.contrib.auth.models import User
from django.db import models


class NOTE(models.Model):
    title = models.TextField(max_length=512, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class NoteShare(models.Model):
    note = models.ForeignKey(NOTE, on_delete=models.PROTECT, null=False, blank=False, related_name='share')
    shared_with = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    status = models.BooleanField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        unique_together = (('note', 'shared_with'),)

