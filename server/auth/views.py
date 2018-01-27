from django.shortcuts import render, redirect
from django.contrib.auth import logout
from decorators import controller_web

# Create your views here.
@controller_web
def login_view(request):
	return render(request, 'base/login.html')

@controller_web
def logout_view(request):
	logout(request)
	return redirect('/')