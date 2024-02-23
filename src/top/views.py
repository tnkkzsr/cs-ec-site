from django.shortcuts import render
from django.views import generic

from items.models import Item


# Create your views here.
class TopView(generic.TemplateView):
    template_name = 'top.html'

# Topページを表示するためのビュー
def TopView(request):
    items_list = Item.objects.all()
    context = {
        "items_list":items_list,
    }
    return render(request, "top.html", context)