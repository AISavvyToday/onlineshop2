from django.shortcuts import render
from .models import Cart
# Create your views here.



def ViewCart(request):
	cart = Cart.objects.all()[0]
	context = {"cart": cart}
	template = "view-cart.html" 


	return render(request, template, context)