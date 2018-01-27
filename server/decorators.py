from keys import *
from django.http import JsonResponse
from django.shortcuts import render

def controller_api(function):
	def wrap(request, *args, **kwargs):
		response = {}
		try:
			return function(request, *args, **kwargs)
		except Exception as e:
			print (e)
			response['success'] = False
			response['message'] = str(e)
			response['response_code'] = RESPONSE_CODE["internal_server_error"]
			return JsonResponse(response)
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap

def controller_web(function):
	def wrap(request, *args, **kwargs):
		response = {}
		try:
			return function(request, *args, **kwargs)
		except Exception as e:
			print (e)
			response['success'] = False
			response['message'] = str(e)
			response['response_code'] = RESPONSE_CODE["internal_server_error"]
			return render(request, 'error/500.html', response)
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap