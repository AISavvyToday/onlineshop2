import re
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.contrib import messages
from . forms import LogInForm, RegistrationForm, UserAddressForm
from . models import EmailConfirmed, USerDefaultAddress

# Create your views here.


def LogOutView(request):
	logout(request)
	messages.success(request, '<strong>Successfully logged out</strong>. Feel free to <a href="%s">login</a> again.' %(reverse("auth_login")), extra_tags="safe")
	return HttpResponseRedirect('%s'%(reverse('auth_login')))



def LogInView(request):
	form = LogInForm(request.POST or None)
	btn ='Login'
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(request, user)
		messages.success(request, 'Successfully logged in, Welcome back!')
		return HttpResponseRedirect('/')
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
		messages.success(request, 'Successfully registered, please check your email for confirmation')
		return HttpResponseRedirect('/')
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
			messages.success(request, 'An error occured with your request')
			return HttpResponseRedirect('/')
		if instance is not None and not instance.confirmed:
			page_message = 'Confirmation Successful, Welcome!'
			instance.confirmed = True
			instance.activation_key = 'Confirmed'
			instance.save()
			messages.success(request, 'Successfully Confirmed, kindly proceed to login')
		elif instance is not None and instance.confirmed:
			messages.success(request, 'Already Confirmed, kindly proceed to login') 
		else:
			page_message = ''
			pass

		context = {'page_message':page_message}
		return render(request, 'activation-complete.html', context)
	else:
		raise Http404


def AddUserAddress(request):
	print(request.GET)
	try:
		next_page = request.GET.get('next')
	except:
		next_page = None
	form = UserAddressForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			new_address = form.save(commit=False)
			new_address.user = request.user
			new_address.save()
			is_default = form.cleaned_data['default']
			if is_default:
				default_address, created = USerDefaultAddress.objects.get_or_create(user=request.user)
				default_address.shipping = new_address
				default_address.save()


			if next_page is not None:
				return HttpResponseRedirect(reverse(str(next_page)))
	submit_btn = 'Save Address'
	form_title = 'Add new address'
	return render(request, 'form.html',\
					context={'form': form,\
					'submit_btn': submit_btn,\
					'form_title': form_title})


















