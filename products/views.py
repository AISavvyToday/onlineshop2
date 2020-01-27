from django.shortcuts import render
from . models import Item, ItemImage
from django.http import Http404
# Create your views here.



def search(request):
	try:
	    q = request.GET.get('q')
	except:
		q = None
	if q:
		items = Item.objects.filter(title__icontains=q)
		context = {"query": q, "items": items}
		template = 'results.html'
	else:
		template = 'home.html'
		context={}
	
	return render(request, template, context)



def home(request):
	items = Item.objects.all()
	context={'items': items }
	return render(request, 'home.html', context)



def all(request):
	items = Item.objects.all()
	context={'items': items }

	return render(request, 'all.html', context)


def single(request, slug):
	try:
		item = Item.objects.get(slug=slug)
		# images = item.itemimage_set.all()
		images = ItemImage.objects.filter(item=item)
		context={'item': item, 'images': images }

		return render(request, 'single.html', context)
	except:
		raise Http404
