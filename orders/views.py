import time

import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from carts.models import Cart
from django.urls import reverse
from . models import Order
from .utils import id_generator
from django.contrib.auth.decorators import login_required
from accounts.forms import UserAddressForm
from accounts.models import UserAddress
# Create your views here.

try:
	stripe_pub = settings.STRIPE_PUBLISHABLE_KEY
	stripe_secret = settings.STRIPE_SECRET_KEY
except Exception:
	raise NotImplementedError(str(e))

stripe.api_key = stripe_secret



def Orders(request):
	context = {}
	return render(request, 'user-orders.html/', context)


@login_required
def Checkout(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
		return HttpResponseRedirect(reverse('cart'))
	try:
		new_order = Order.objects.get(cart=cart)
	except Order.DoesNotExist:
		new_order = Order()
		new_order.cart = cart
		new_order.user = request.user
		new_order.order_id = id_generator()
		 
		new_order.save()
	except:
		new_order = None 
		return HttpResponseRedirect(reverse('cart'))
	final_amount = 0
	if new_order is not None:
		new_order.sub_total = cart.total
		new_order.save()
		final_amount = new_order.get_final_amount() 
	try:
		address_added = request.GET.get('address_added')
	except:
		address_added = None
	if address_added is None:
		address_form = UserAddressForm()
	else:
		address_form = None

	current_addresses = UserAddress.objects.filter(user=request.user)
	billing_addresses = UserAddress.objects.get_billing_addresses(user=request.user)

	if request.method == 'POST':
		try:
			user_stripe = request.user.userstripe.stripe_id
			customer = stripe.Customer.retrieve(user_stripe)
		except:
			customer = None
			pass
		if customer is not None:
			card = stripe.Customer.create_source(user_stripe,source="tok_mastercard")	
			card.save()
			charge = stripe.Charge.create(amount=int( final_amount * 100),currency="usd",card=card,\
				customer=customer)

			if charge['captured']:
				new_order.status = 'Finished'
				new_order.save()
				del request.session['cart_id']
				del request.session['total_items']
				messages.success(request,'Your order has been successfully completed,\
					thank you for shopping with us')
				return HttpResponseRedirect(reverse('user-orders'))


	context = { 'order': new_order,
				'address_form':address_form,
				'current_addresses':current_addresses,
				'billing_addresses': billing_addresses,
				'stripe_pub': stripe_pub,

	}
	return render(request, 'checkout.html', context)






