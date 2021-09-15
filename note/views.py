from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated

from TecNotesPlus import Pagination
from TecNotesPlus.viewset import CustomViewSetForQuerySet
from note.models import NOTE, NoteShare


class NoteSerializer(serializers.ModelSerializer):
    created_user_name = serializers.StringRelatedField(source='created_by.username')

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
        queryset = queryset.filter(created_by=self.request.user)
        # printer_name = self.request.GET.get('printer_name')
        # toner_name = self.request.GET.get('toner_name')
        # remove_duplicate_printer = self.request.GET.get('remove_duplicate_printer')
        #
        # if printer_name:
        #     queryset = queryset.filter(printer_model=printer_name)
        #
        # if toner_name:
        #     queryset = queryset.filter(toner_model=toner_name)
        #
        # if remove_duplicate_printer and bool(remove_duplicate_printer) is True:
        #     queryset = queryset.distinct('printer_model')

        return queryset


class NoteShareSerializer(serializers.ModelSerializer):
    shared_with_username = serializers.StringRelatedField(source='shared_with.username')
    note_title = serializers.StringRelatedField(source='note.title')
    status_label = serializers.SerializerMethodField()

    def get_status_label(obj):
        if obj.status:
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
        # printer_name = self.request.GET.get('printer_name')
        # toner_name = self.request.GET.get('toner_name')
        # remove_duplicate_printer = self.request.GET.get('remove_duplicate_printer')
        #
        # if printer_name:
        #     queryset = queryset.filter(printer_model=printer_name)
        #
        # if toner_name:
        #     queryset = queryset.filter(toner_model=toner_name)
        #
        # if remove_duplicate_printer and bool(remove_duplicate_printer) is True:
        #     queryset = queryset.distinct('printer_model')

        return queryset



class NoteView(TemplateView):
    template_name = 'note/note_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super(WeekendHoliday, self).get_context_data(**kwargs)
    #     context['weekend_form'] = modelform_factory(Weekend, exclude=[])()
    #     context['holiday_form'] = modelform_factory(Holiday, exclude=[])()
    #     context['weekend_list'] = list(Weekend.objects.all().values_list('day', flat=True))
    #     context['holiday_list'] = list(Holiday.objects.all().values_list('date', flat=True))
    #
    #     return context


class NoteShareView(TemplateView):
    template_name = 'note/note_share.html'