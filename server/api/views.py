from django.shortcuts import render
from django.http import JsonResponse
from decorators import controller_api
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.http import HttpResponse
from appProfile.models import Profile
from keys import *
import jwt
import json
from notice.models import *

# Create your views here.

@csrf_exempt
@controller_api
def register(request):
	response = {}
	print(request.body)
	body = json.loads(request.body.decode('utf-8'))
	temp_first_name = body['firstName']
	temp_last_name = body['lastName']
	temp_email = body['email']
	temp_roll_no = body['rollNumber']
	temp_password = body['password']
	temp_username = temp_roll_no
	user = User.objects.create_user(temp_username, temp_email, temp_password)
	user.first_name = temp_first_name
	user.last_name = temp_last_name
	user.save()
	user.profile.roll_number = temp_roll_no
	user.save()
	json_dump = {}
	json_dump['user_id'] = user.pk
	json_dump['username'] = user.username
	json_dump['roll_number'] = user.profile.roll_number
	token = jwt.encode(json_dump, TOKEN_SECRET, algorithm='HS256')
	token = str(token)
	response['success'] = True
	response['message'] = "Profile created successfully"
	response['response_code'] = RESPONSE_CODE["success"]
	response['token'] = token
	return JsonResponse(response)

@csrf_exempt
@controller_api
def login(request):
	response = {}
	body = json.loads(request.body.decode('utf-8'))
	temp_roll_no = body['rollNumber']
	temp_password = body['password']
	user = authenticate(username=temp_roll_no, password=temp_password)
	if user is not None:
		json_dump = {}
		json_dump['user_id'] = user.pk
		json_dump['username'] = user.username
		json_dump['roll_number'] = temp_roll_no
		token = jwt.encode(json_dump, TOKEN_SECRET, algorithm='HS256')
		token = str(token)
		response['success'] = True
		response['message'] = 'Login Successfull !'
		response['response_code'] = RESPONSE_CODE["success"]
		response['token'] = token
	else : 
		response['success'] = False
		response['message'] = 'Wrong Credentials'
		response['response_code'] = RESPONSE_CODE["forbidden"]
	return JsonResponse(response)

@csrf_exempt
@controller_api
def notice(request):
	response = {}
	all_notice = Notice.objects.filter(status=True)

	notice_list = []
	temp_meta = {}
	temp_meta['image'] = str("http://127.0.0.1:8000/static/assets/img/new_logo.png")
	for obj in all_notice:
		temp_data = {
			'id': obj.id,
			'title': obj.title,
			'description':obj.description,
			'meta':temp_meta,
			'start_date': obj.start_date,
			'end_date': obj.end_date,
		}

		notice_list.append(temp_data)
		temp_data = {}


	data = {
	'success' : True,
	'data' : notice_list
	}	

	return JsonResponse(data)
