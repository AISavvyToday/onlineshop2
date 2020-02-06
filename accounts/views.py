import re
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import logout, login, authenticate
from . forms import LogInForm, RegistrationForm
from . models import EmailConfirmed

# Create your views here.


def LogOutView(request):
	logout(request)
	return HttpResponseRedirect('/')



def LogInView(request):
	form = LogInForm(request.POST or None)
	btn ='Login'
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(request, user)
	context = {
		'form': form,
		'submit_btn': btn
	}
	return render(request, 'form.html', context)



def RegisterView(request):
	form = RegistrationForm(request.POST or None)
	btn ='Join'
	if form.is_valid():
		new_user = form.save(commit=False)
		# new_user.first_name = 'Winnie' # customize model form
		new_user.save()
		# username = form.cleaned_data['username']
		# password = form.cleaned_data['password']
		# user = authenticate(username=username, password=password)
		# login(request, user)
	context = {
	'form': form,
	'submit_btn': btn
	}
	return render(request, 'form.html', context)



SHA1_RE = re.compile('^[a-f0-9]{40}$')

def ActivationView(request, activation_key):
	if SHA1_RE.search(activation_key):
		try:
			instance = EmailConfirmed.objects.get(activation_key=activation_key)
		except EmailConfirmed.DoesNotExist:
			instance = None
			raise Http404
		if instance is not None and not instance.confirmed:
			page_message = 'Confirmation Successful, Welcome!'
			instance.confirmed = True
			instance.activation_key = 'Confirmed'
			instance.save()
		elif instance is not None and instance.confirmed:
			page_message = 'Already confirmed' 
		else:
			page_message = ''
			pass

		context = {'page_message':page_message}
		return render(request, 'activation-complete.html', context)
	else:
		raise Http404


















