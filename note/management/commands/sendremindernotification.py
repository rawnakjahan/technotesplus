from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from TecNotesPlus import settings
from note.models import NoteShare


class Command(BaseCommand):
    help = 'Send reminder notification.'

    def handle(self, *args, **options):
        current_day = timezone.now().date()
        unseen_shares = NoteShare.objects.filter(created_at__date__lt=current_day, status=0)
        for share in unseen_shares:
            # global delegation options
            User.objects.get(id=share.shared_with_id).email_user(
                subject="Note Shared",
                message="Dear Sir/Madam, You have missed a new note from {}.".format(share.note.created_by.username),
                from_email=settings.EMAIL_HOST_USER)
            self.stdout.write(self.style.SUCCESS('Mail send successful to "{}".').format(User.objects.get(id=share.shared_with_id).email))
