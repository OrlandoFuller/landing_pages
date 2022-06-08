# from django.shortcuts import render
from django.views.generic import TemplateView

class BackgroundView(TemplateView):
    template_name = 'background.html'
