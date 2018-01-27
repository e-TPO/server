from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from decorators import controller_api
import json
import csv

# Create your views here.
def index(request):
	return render (request, 'base/home.html')

@csrf_exempt
@controller_api
def create_placement(request):
	print(request.body.decode('utf-8'))
	
	body = json.loads(request.body)

	data = {
	'success':True
	}

	return JsonResponse(data)

def redirect(request):
	return redirect('/placement')

