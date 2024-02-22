from django.shortcuts import render
from .forms import Add_Item_Form
from .models import Item


def Add_Item_page(request):
    form = Add_Item_Form(request.POST)
    return render(request, 'items/add_item.html', {'form': form})


def Add_Item_Completed(request):
    form = Add_Item_Form(request.POST)
    
    if request.method == "POST":
            if form.is_valid():
                item_title = form.cleaned_data['item_title']
                item_explain = form.cleaned_data['item_explain']
                item_category = form.cleaned_data['item_category']
                item_condition = form.cleaned_data['item_condition']
                item_price = form.cleaned_data['item_price']
                # seller = request.user
                Item.objects.create(
                    item_title=item_title,
                    item_explain=item_explain,
                    item_category=item_category,
                    item_condition=item_condition,
                    item_price=item_price,
                    # seller=seller
                )
                return render(request, 'items/add_item_completed.html')
            else:
                pass