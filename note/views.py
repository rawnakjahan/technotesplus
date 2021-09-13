from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, serializers
from note.models import NOTE


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NOTE
        fields = '__all__'


class NoteViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = NOTE.objects.all()


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