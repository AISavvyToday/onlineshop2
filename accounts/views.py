from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from . forms import LogInForm

# Create your views here.


def LogOutView(request):
	logout(request)
	return HttpResponseRedirect('/')



def LogInView(request):
	form = LogInForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(request, user)
	context = {
		'form': form
	}
	return render(request, 'form.html', context)