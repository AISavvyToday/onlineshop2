from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from . models import Cart, CartItem
from products.models import Item, Variation
# Create your views here.



def ViewCart(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
	if the_id:
		new_total = 0.00
		for i in cart.cartitem_set.all():
			item_line_total = float(i.item.price) * i.quantity
			new_total += item_line_total
		request.session['total_items'] = cart.cartitem_set.count()
		cart.total = new_total
		cart.save()
		context = {"cart": cart} 
	else:
		empty_cart_message = 'Your cart is currently empty, please keep shopping'
		context = {"empty": True, "empty_cart_message": empty_cart_message }
	template = "view-cart.html" 
	return render(request, template, context)


def RemoveFromCart(request,id):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		return HttpResponseRedirect(reverse("cart"))

	cartitem = CartItem.objects.get(id=id)
	cartitem.cart = None
	cartitem.save()
	# cartitem.delete()
	# send success message
	return HttpResponseRedirect(reverse("cart"))

 


def AddToCart(request, slug):
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

	item_var = [] #product variation	
	if request.method == "POST":
		Qty = request.POST['Qty']
		for i in request.POST:
			key = i
			value = request.POST[key]
			try:
				v = Variation.objects.get(item=item, category__iexact=key, title__iexact=value)
				item_var.append(v)
			except:
				pass

	
		cart_item = CartItem.objects.create(cart=cart, item=item)
		if len(item_var) > 0:
			cart_item.variations.add(*item_var)
		cart_item.quantity = Qty
		cart_item.save()
		#success message


		return HttpResponseRedirect(reverse("cart"))
	# error message
	return HttpResponseRedirect(reverse("cart"))