from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from django.utils import timezone

from core.models import *

class SongDetailView(DetailView):

    model = Song

    def get_context_data(self, **kwargs):
        context = super(SongDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context