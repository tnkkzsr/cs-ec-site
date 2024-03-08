
import payjp
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from account.models import PaymentInfo, User, User_Additional_Address
from items.models import Item

from .models import Trade


# Create your views here.
@login_required
def confirm(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    user = get_object_or_404(User, pk=request.user.pk)
    request.session['item'] = item_id
    if request.method == 'POST':
        Address = request.POST.get("Address")
        request.session["address"] = Address
        return redirect('settlement:payment')
    else:
        addresses = [user.address]
        AdditionalAddresses = User_Additional_Address.objects.filter(user=request.user.pk)
        for address in AdditionalAddresses:
            addresses.append(address)
        
        return render(request, 'settlement/AddressSelect.html', {'item':item, 'addresses':addresses})

def completed(request):

    return render(request, 'settlement/completed.html')

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['user_id']

class AddAddress(OnlyYouMixin, generic.TemplateView):
    template_name = 'settlement/AddAddress.html'

    def post(self, request, user_id):
        AdditionalAddress =  request.POST.get("address")
        user = get_object_or_404(User, pk=user_id)
        NewAddress = User_Additional_Address(user=user, additional_address=AdditionalAddress)
        NewAddress.save()
        item_id = request.session['item']
        print(request.POST.get("item_price"))
        return redirect('settlement:AddressSelect', item_id=item_id)


def stripe(request):
    item = request.session['item']
    address = request.session['address']
    return render(request, 'settlement/stripe.html', {'item':item, 'address':address})

class PayView(generic.View):
    """
    use PAY.JP API
    """
    
    def get(self, request):
        item = get_object_or_404(Item, pk=request.session['item'])
        amount = item.item_price
        # 公開鍵を渡す
        context = {"public_key": "pk_test_eec2c84ed893ec3da8110866",
                   "amount": amount,
                   }
        return render(
            request, "settlement/confirm.html", context
        )

    def post(self, request):
        item = get_object_or_404(Item, pk=request.session['item'])
        amount = item.item_price
        payjp_token = request.POST.get("payjp-token")

        # トークンから顧客情報を生成
        customer = payjp.Customer.create(email=request.user.email, card=payjp_token)
        # 支払いを行う
        charge = payjp.Charge.create(
            amount=amount,
            currency="jpy",
            customer=customer.id,
            description="Django example charge",
        )
        Trade.objects.create(item=item, purchaser=request.user, price=amount)
        
        #TODO 購入した商品を消去する
        
        context = {"amount": amount, "customer": customer, "charge": charge}
        return render(request, "settlement/completed.html", context)