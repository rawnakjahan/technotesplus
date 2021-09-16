from django.contrib.auth.models import User
from django.core.mail import send_mail, get_connection, EmailMultiAlternatives
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from TecNotesPlus import Pagination
from TecNotesPlus.viewset import CustomViewSetForQuerySet
from note.models import NOTE, NoteShare
import TecNotesPlus.settings as settings


class NoteSerializer(serializers.ModelSerializer):
    created_user_name = serializers.StringRelatedField(source='created_by.username')
    share_with = serializers.SerializerMethodField()
    seen_status = serializers.SerializerMethodField()

    def get_share_with(self, obj):
        return User.objects.filter(id__in=obj.share.all().values_list('shared_with', flat=True)).values_list('username',
                                                                                                             flat=True)

    def get_seen_status(self, obj):
        obj_status = True
        request = self.context.get('request', None)
        try:
            s = obj.share.get(note_id=obj.id, shared_with=request.user)
            if not s.status:
                obj_status = False
        except Exception:
            print("Status not Found")
        return obj_status

    class Meta:
        model = NOTE
        fields = '__all__'


class NoteViewSet(CustomViewSetForQuerySet):
    model = NOTE
    serializer_class = NoteSerializer
    pagination_class = Pagination.LargeResultsSetPagination
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAuthenticated]
    permission_id = [0]

    # search_keywords = ('toner_model', 'printer_model')

    def get_queryset(self):
        queryset = super().get_queryset()
        shared_note_ids = NoteShare.objects.filter(shared_with=self.request.user).distinct().values_list('note_id',
                                                                                                         flat=True)
        print("shared_note_ids", shared_note_ids)
        queryset = queryset.filter(Q(created_by=self.request.user) | Q(id__in=shared_note_ids))
        return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if self.check_validation(instance):
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.check_validation(instance):
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

    def check_validation(self, obj):
        if not self.request.user == obj.created_by:
            raise serializers.ValidationError(
                {'detail': 'You are not permitted to Update or Delete this information'})
        return True


class NoteShareSerializer(serializers.ModelSerializer):
    shared_with_username = serializers.StringRelatedField(source='shared_with.username')
    note_title = serializers.StringRelatedField(source='note.title')
    status_label = serializers.SerializerMethodField()

    def get_status_label(self, obj):
        if obj.status == 0:
            return "Seen"
        else:
            return "Not Seen"

    class Meta:
        model = NoteShare
        fields = '__all__'


class NoteShareViewSet(CustomViewSetForQuerySet):
    model = NoteShare
    serializer_class = NoteShareSerializer
    pagination_class = Pagination.LargeResultsSetPagination
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAuthenticated]
    permission_id = [0]

    # search_keywords = ('toner_model', 'printer_model')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(note__created_by=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # send mail notification
        User.objects.get(id=serializer.data['shared_with']).email_user(
            subject="Note Shared",
            message="Dear Sir/Madam, You have a new note from {}.".format(self.request.user.username),
            from_email=settings.EMAIL_HOST_USER)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_note_share_status(request):
    note_id = request.data.get('note_id', None)
    try:
        instance = NoteShare.objects.get(note_id=note_id, shared_with=request.user)
        instance.status = True
        instance.save()
        return Response({'status': 'success', 'message': 'Status updated successfully'}, status=200)
    except Exception():
        return Response({'status': 'error', 'message': 'Data match not found'}, status=400)


class NoteView(TemplateView):
    template_name = 'note/note_list.html'

    def get_context_data(self, **kwargs):
        context = super(NoteView, self).get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        print(context['user_list'])
        return context


class NoteShareView(TemplateView):
    template_name = 'note/note_share.html'
