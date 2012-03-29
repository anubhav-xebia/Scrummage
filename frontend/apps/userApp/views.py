from django.http import HttpResponse
from django.core.context_processors import csrf
#from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from lib.Request import APIRequest
from apps.settings import api_url_register
import datetime

def home(request):
    return render_to_response('homepage.html', context_instance=RequestContext(request))

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('homepage.html', c)

def register(request):
	requestData = {}
	requestData.setdefault('email', request.POST['email'])
	requestData.setdefault('password', request.POST['password'])
	requestData.setdefault('repassword', request.POST['repassword'])
	
	response = APIRequest(api_url_register, requestData).getResponse()

	# create api request to register the user
	print response
	
	c = {}
	c.update(csrf(request))
	return render_to_response('homepage.html', c)
