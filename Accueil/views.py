from django.shortcuts import render
from django.views.generic.base import TemplateView
from Photographies.models import Photo


class AccueilTemplateView(TemplateView):

    template_name = "Accueil.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo'] = Photo.objects.all().order_by('-Date')[0]

        return context
