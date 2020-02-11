import json
import datetime
from django.conf import settings
from django.utils import timezone
from django.shortcuts import render, HttpResponse, Http404
from django.http import HttpResponseBadRequest
from .forms import EmailForm
from accounts.models import EmailMarketingSignUp


# Create your views here.

def DismissMarketingMessage(request):
	if request.is_ajax():
		data = {}
		print(data)
		json_data = json.dumps(data)
		request.session['dismiss_message_for'] = str(timezone.now() +\
			datetime.timedelta(hours=settings.MARKETING_HOURS_OFFSET,\
				seconds=settings.MARKETING_SECONDS_OFFSET))
		print(json_data)
		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404

def EmailSignUp(request):
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			new_signup = EmailMarketingSignUp.objects.create(email=email)
			request.session['email_added_marketing'] = True
			return HttpResponse('Success %s' %(email))
		if form.errors:
			json_data = json.dumps(form.errors)
			return HttpResponseBadRequest(json_data, content_type='application/json')
	else:
		raise Http404






