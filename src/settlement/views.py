import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from items.models import Item
from account.models import User, User_Additional_Address, PaymentInfo

# Create your views here.
@login_required
def confirm(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    user = get_object_or_404(User, pk=request.user.pk)
    request.session['item'] = item_id
    if request.method == 'POST':
        Address = request.POST.get("Address")
        request.session["address"] = Address
        return redirect('settlement:stripe')
    else:
        addresses = [user.address]
        AdditionalAddresses = User_Additional_Address.objects.filter(user=request.user.pk)
        for address in AdditionalAddresses:
            addresses.append(address)
        
        return render(request, 'settlement/index.html', {'item':item, 'addresses':addresses})

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
        return redirect('settlement:confirm', item_id=item_id)


@require_POST
@csrf_exempt
def create_checkout_session(request):
    user = request.user
    price_id = json.loads(request.body)
    email = request.user.get_email()

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            customer_email=email,
            allow_promotion_codes=True,
            success_url=DOMAIN + 'subscription?session_id={'
                                  'CHECKOUT_SESSION_ID}',
            cancel_url=DOMAIN + 'checkout'
        )

        return JsonResponse({'id': checkout_session.id})