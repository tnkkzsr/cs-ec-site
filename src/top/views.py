from django.shortcuts import render
from django.views import generic

# Create your views here.
class TopView(generic.TemplateView):
    template_name = 'top.html'