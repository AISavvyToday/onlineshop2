from django.shortcuts import render
from . models import Item

# Create your views here.

def home(request):
	context=locals()

	return render(request, 'home.html', context)




def all(request):
	items = Item.objects.all()
	context={'items': items }

	return render(request, 'all.html', context)
	
