from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from . forms import LogInForm, RegistrationForm


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
		user.emailconfirmed.activate_user_email()
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