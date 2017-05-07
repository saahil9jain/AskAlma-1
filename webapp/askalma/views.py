from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect
from .models import *
from django.shortcuts import render
import time
from elasticsearch import Elasticsearch
from urlparse import urlparse
import gdata.client
import gdata.gauth
import json
import gdata.photos.service #In this example where contacting Google Picasa Web API



es = Elasticsearch("search-askalma-ec4hakudbwu54iw5gnp6k6ggpy.us-east-1.es.amazonaws.com", port=443,
				   use_ssl='true')


def _isLoggedIn(request):
	try:
		email = request.session['email']
		last_in = request.session['last_in']
		#Thirty minute old sessions are killed
		if (time.time()- last_in > 1800):
			return HttpResponseRedirect(reverse('social:begin' ,args=('google-oauth2',)))
		request.session['last_in'] = time.time()
		return None
	except KeyError:
		return HttpResponseRedirect(reverse('social:begin' ,args=('google-oauth2',)))


def index(request):
	#Add these two lines to any page that requires user to be logged in
	result = _isLoggedIn(request)
	if result != None: return result
	context = {}
	context['stats'] = _getStats()
	return render(request, 'askalma/index.html', context=context)

class QDetailView (generic.DetailView):
    template_name = "askalma/qdetail.html"

def listing(request):
	context = {}
	return render(request, 'askalma/listing.html' , context = context)

def postquestion(request):
	return render(request, 'askalma/post-question.html')

def profile (request):
	result = _isLoggedIn(request)
	if result != None: return result

	user_info = _get_user_profile (request.session['email'])
	context = {'user_info' : user_info}
	print context
	return render(request, 'askalma/profile.html' , context)

def edit_profile (request ):
	result = _isLoggedIn(request)
	if result != None: return result

	user_info =_get_user_profile (request.session['email'])
	context = {'user_info' : user_info}
	return render(request , 'askalma/profile-setting.html', context= context)

def logout(request):
	try:
		del request.session['email']
	except:
		pass
	return index(request)

def contactus (request):
	pass


def qdetail(request):
	context = {}
	return render(request, 'askalma/question_detail.html', context = context)


#JUST UNCOMMENT the two lines
def _getStats ():
	stats = {}
	stats['views'] = 7812
	#stats['questions'] = es.search(index='questions', body={"size": 0,})['hits']['total']
	# stats['answersed_questions'] = es.search(index='questions', body={"size": 0,"query":{ "query_string": { "query": 1, "default_field": 'answered' }}})['hits']['total']
	stats['users'] =  es.search(index='users', body={"size": 0,})['hits']['total']
	stats['questions'] = 232
	stats['answered_questions'] = 147

	return stats

def autherror(request):
	#While this should an error page, it seems that it is nothing too serious, just redirect to index
	return index(request)


def process_auth(details,strategy,request,**kwargs):
	#Add user info to session, to keep them logged in
	strategy.session_set('email', details['email'])
	strategy.session_set('last_in', time.time())
	strategy.session_set('first_name', details['first_name'])
	strategy.session_set('last_name', details['last_name'])
	#Check if they exist in ES. IF not, add them.
	count = es.search(index='users', body={"size": 0,"query":{ "query_string": { "query": details['email'] , "default_field": 'email' }}})['hits']['total']
	if count == 0:
		doc = {
			"email": details['email'],
			"first_name" : details['first_name'],
			"last_name": details['last_name'],
			"headline" : "Student at Columbia University"
		}
		es.index(index="users", doc_type='user', body=doc)

def _get_user_profile (email):
	res = es.search(index='users', body={"from": 0, "size": 1, "query": {
		"query_string": {"query": email, "default_field": 'email'}}})
	print res
	return res['hits']['hits'][0]['_source']
