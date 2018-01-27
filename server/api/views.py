from django.shortcuts import render
from django.http import JsonResponse
from decorators import controller_api
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.http import HttpResponse
from appProfile.models import Profile
from placement.models import PlacementSession
from keys import *
import jwt
import json
from notice.models import *
from article.models import *

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
	# print(body)
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
def get_notices(request):
	response = {}
	all_notice = Notice.objects.filter(status=True)

	notice_list = []
	temp_meta = {}
	temp_meta['image'] = str("http://127.0.0.1:8000/static/assets/img/new_logo.png")
	for obj in all_notice:
		temp_data = {}
		temp_data['id'] = obj.id,
		temp_data['title'] = obj.title,
		temp_data['description'] =obj.description,
		temp_data['meta'] =temp_meta,
		temp_data['start_date'] = obj.start_date,
		temp_data['end_date'] = obj.end_date,

		notice_list.append(temp_data)
		temp_data = {}


	data = {}
	data['success'] = True
	data['data'] = notice_list
	return JsonResponse(data)

@csrf_exempt
@controller_api
def get_articles(request):
	response = {}
	temp_articles = Article.objects.all()

	articles_list = []
	temp_article = {}
	for atkl in temp_articles:
		temp_article = {}
		temp_article['title'] = str(atkl.title)
		temp_article['summary'] = str(atkl.summary)
		temp_article['body'] = str(atkl.body)
		temp_article['url'] = str(atkl.url)
		articles_list.append(temp_article)
		temp_article = {}

	response['success'] = True
	response['data'] = articles_list
	return JsonResponse(response)

@csrf_exempt
@controller_api
def get_notifications(request):
	response = {}
	temp_token = request.POST.get('token')
	temp_token = jwt.encode(temp_token, TOKEN_SECRET, algorithm='HS256')

@csrf_exempt
@controller_api
def get_placement_sessions(request):
	response = {}
	if PlacementSession.objects.filter(status=True).exists():
		temp_placements_session = PlacementSession.objects.filter(status=True)
		placements_session_list = []
		temp_placement_session = {}
		for session in temp_placements_session:
			temp_placement_session = {}
			temp_placement_session['id'] = session.pk
			temp_placement_session['company'] = str(session.company)
			temp_placement_session['title'] = str(session.title)
			temp_placement_session['description'] = session.description
			temp_placement_session['requirements'] = session.requirements
			temp_placement_session['rounds'] = session.rounds
			placements_session_list.append(temp_placement_session)
			temp_placement_session = {}

		response['success'] = True
		response['data'] = placements_session_list
	else:
		response['success'] = False
		response['data'] = "It seems like there is no live placement session"
	return JsonResponse(response)

# @csrf_exempt
# @controller_api
# def update_profile(requests):
# 	response = {}
# 	body = json.loads(request.body.decode('utf-8'))
# 	temp_email = body['email']
# 	temp_contact_number = body['contactNumber']
# 	temp_bio = body['bio']
# 	temp_