from django.db import models
from .models import MarketingMessage


class DisplayMarketingMessage:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_request(self, request):
		pass

		# try:
		# 	request.session['marketing_message'] = MarketingMessage.objects.all()[0].message
		# except:
		# 	request.session['marketing_message'] = False

		# return request.session['marketing_message']

		

		
