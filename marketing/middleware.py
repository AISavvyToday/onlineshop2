
from django.db import models
from .models import MarketingMessage



class DisplayMarketingMessage(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		return self.get_response(request)

	def process_request(self, request):
		try:
			request.session['marketing_message'] = MarketingMessage.objects.get_featured_item().message
		except:
			request.session['marketing_message'] = False




		
