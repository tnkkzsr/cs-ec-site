from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import Add_Item_Form
from .models import Item

from rest_framework.views import APIView
from rest_framework.response import Response


# 商品を出品するフォームページを表示するビュー
@login_required
def Add_Item_page(request):
    # フォームが送信された場合
    if request.method == "POST":
        form = Add_Item_Form(request.POST, request.FILES)
        if form.is_valid():
            item_title = form.cleaned_data['item_title']
            item_explain = form.cleaned_data['item_explain']
            item_category = form.cleaned_data['item_category']
            item_condition = form.cleaned_data['item_condition']
            item_price = form.cleaned_data['item_price']
            item_image = form.cleaned_data['item_image']
            seller = request.user
            Item.objects.create(
                item_title=item_title,
                item_explain=item_explain,
                item_category=item_category,
                item_condition=item_condition,
                item_price=item_price,
                seller=seller,
                item_image=item_image,
            )
            return redirect('items:add_item_completed')
    else:
        form = Add_Item_Form()
    
    return render(request, 'items/add_item.html', {'form': form})


# 商品追加完了ページへのビュー
def Add_Item_Completed(request):
    
    return render (request, 'items/add_item_completed.html')


def Item_Detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST' and request.POST.get('action') == 'like':
        current_likes = request.session.get('likes', 0)
        new_likes = current_likes + 1
        request.session['likes'] = new_likes

        # 応答を作成して返す
        return JsonResponse({'success': True, 'likes': new_likes})
    else:
        return render(request, 'items/item_detail.html', {'item':item})
    
# 商品のいいねをするためのビュー
class LikeItem(APIView):
    def post(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        
        # ユーザーがまだいいねしていない場合のみitem.likesを増やす
        if not item.LikeUsers.filter(pk=request.user.pk).exists():
            item.LikeUsers.add(request.user)
            item.likes += 1
            request.session['likes'] = item.likes
            item.save()
        
        else:
            user = get_object_or_404(item.LikeUsers, pk=request.user.pk)
            item.LikeUsers.remove(user)
            item.likes -= 1
            request.session['likes'] = item.likes
            item.save()

        return Response({'success': True, 'likes': item.likes})
        
        