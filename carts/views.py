from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from . models import Cart
from products.models import Item
# Create your views here.



def ViewCart(request):
	try:
		the_id = request.session['cart_id']
	except:
		the_id = None
	if the_id:
		cart = Cart.objects.get(id=the_id)
		context = {"cart": cart} 
	else:
		empty_cart_message = 'Your cart is currently empty, please keep shopping'
		context = {"empty": True, "empty_cart_message": empty_cart_message }
	template = "view-cart.html" 
	return render(request, template, context)




def UpdateCart(request, slug):
	request.session.set_expiry(600)
	try:
		the_id = request.session['cart_id']
	except:
		#create cart
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id
	cart = Cart.objects.get(id=the_id)
	try:
		item = Item.objects.get(slug=slug)
	except Item.DoesNotExist:
		pass
	except:
		pass
	if not item in cart.items.all():
		cart.items.add(item)
	else:
		cart.items.remove(item)
	new_total = 0.00
	for item  in cart.items.all():
		new_total += float(item.price)
	request.session['total_items'] = cart.items.count()
	cart.total = new_total
	cart.save()

	return HttpResponseRedirect(reverse("cart"))