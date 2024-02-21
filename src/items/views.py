from django.shortcuts import render


def Additem(request):
    # form = AddItemForm(request.POST)
    
    # if request.method == "POST":
    #         if form.is_valid():
    #             item_title = form.cleaned_data['item_title']
    #             item_explain = form.cleaned_data['item_explain']
    #             item_category = form.cleaned_data['item_category']
    #             item_condition = form.cleaned_data['item_condition']
    #             item_price = form.cleaned_data['item_price']
    #             seller = request.user
    #             item, created = Item.objects.update_or_create(
    #                 reviewer = reviewer,
    #                 book = book,
                    
    #                 defaults={
    #                     'book': book,'review_text': review_text,'score': score,'reviewer': reviewer,'review_title': review_title
    #                 }
    #             )
    #             return HttpResponseRedirect(reverse("book:detail", args=[book_id]))
    #         else:
    #             pass
            

    return render(request, 'items/add_item.html')