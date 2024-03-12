from django.shortcuts import render
from django.views import generic
from django.db.models import Q

from items.models import Item


# Create your views here.
class TopView(generic.TemplateView):
    template_name = 'top.html'

# Topページを表示するためのビュー
def TopView(request):
    if request.method == "POST":
        SearchWord = request.POST.get("search")
        print(SearchWord)
        items_list = Item.objects.filter(
            Q(item_title__contains=SearchWord) |
            Q(item_explain__contains=SearchWord)
        )
    else:
        items_list = Item.objects.all()
    context = {
        "items_list":items_list,
    }
    return render(request, "top.html", context)