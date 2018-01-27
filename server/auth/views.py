from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout, authenticate, login
from decorators import controller_web
from django.template import RequestContext

# Create your views here.
@controller_web
def login_view(request):
	if request.method == 'POST':
		temp_roll_no = request.POST.get('username')
		temp_password = request.POST.get('password')
		user = authenticate(username=temp_roll_no, password=temp_password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			context = {}
			context['message'] = "Please check your roll number and password again."
			return render(request, 'base/login.html', context)
	else:
		return render(request, 'base/login.html')

@controller_web
def logout_view(request):
	logout(request)
	return redirect('/')

@controller_web
def signup_view(request):
	return render(request, 'base/signup.html')

def handler404(request):
	response = render_to_response('error/404.html', {},context_instance=RequestContext(request))
	response.status_code = 404
	return response

def handler500(request):
	response = render_to_response('error/500.html', {},context_instance=RequestContext(request))
	response.status_code = 500
	return response