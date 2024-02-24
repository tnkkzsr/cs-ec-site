from django.shortcuts import redirect, render

from .forms import Add_Item_Form
from .models import Item


# 商品を出品するフォームページを表示するビュー
def Add_Item_page(request):
    # フォームが送信された場合
    if request.method == "POST":
        form = Add_Item_Form(request.POST)
        if form.is_valid():
            item_title = form.cleaned_data['item_title']
            item_explain = form.cleaned_data['item_explain']
            item_category = form.cleaned_data['item_category']
            item_condition = form.cleaned_data['item_condition']
            item_price = form.cleaned_data['item_price']
            seller = request.user
            Item.objects.create(
                item_title=item_title,
                item_explain=item_explain,
                item_category=item_category,
                item_condition=item_condition,
                item_price=item_price,
                seller=seller
            )
            return redirect('items:add_item_completed')
    else:
        form = Add_Item_Form()
    
    return render(request, 'items/add_item.html', {'form': form})


# 商品追加完了ページへのビュー
def Add_Item_Completed(request):
    
    return render (request, 'items/add_item_completed.html')