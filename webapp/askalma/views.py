from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django.template import RequestContext
from django.urls import reverse
from django.shortcuts import redirect
from .models import *
from django.shortcuts import render
import time
from django.views.decorators.csrf import csrf_exempt
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


#def getanswers(request):


class QDetailView (generic.DetailView):
    template_name = "askalma/qdetail.html"

def listing(request):
	context = {}
	#print request
	response= searchquestion(request)
	#print response
	if response.get('questions')== "nothing": return response
	return render(request, 'askalma/listing.html' , context = context)


def searchquestion(request):
	try:
		#print "taking questions from elasticsearch"
		result=es.search(index='questions1', body={"from" : 0, "size" : 1000, "query":{"match_all": {}}})
		#print result
		questions= result['hits']['hits']
		#print questions
		b= []
		for question in questions:
			#print question
			tags= question['_source']['tags']
			taglist= [s.strip() for s in tags.split(',')]
			a = {
			"title": question['_source']['title'],
			"taglist": taglist,
			"details": question['_source']["details"]
			}
			b.append(a)
		#print b
		return JsonResponse({'questions': b })
	except KeyError:
		return JsonResponse({'questions': "nothing"})

@csrf_exempt
def postquestion(request):
	#print "in postquestion"
	#print request
	#print ("inside HTML page")
	#print request
	result = pullquestion(request)
	if result== "data":
		#print "Added to ES"
		return render(request, 'askalma/listing.html')
	else:
		return render(request, 'askalma/post-question.html')

def pullquestion(request):
	try:
		#print "sending question to elasticsearch"
		title= str(request.GET.get("title", ' '))
		#print title
		tags= str(request.GET.get("tags", ' '))
		#print tags
		details= str(request.GET.get("details", ' '))
		#print details
		#print "inside es working"
		doc = {
			"title": title,
			"tags": tags,
			"details": details
		}
		#print doc
		if title!=" ":
			es.index(index="questions1", doc_type='question', body=doc)
		return HttpResponseRedirect("data")
	except KeyError:
		return HttpResponseRedirect("webpage")

def profile (request):
	result = _isLoggedIn(request)
	if result != None: return result

	user_info = _get_user_profile (request.session['email'])
	context = {'user_info' : user_info}
	#print context
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

@csrf_exempt
def qdetail(request):
	context = {}
	#print "request"
	result= getanswers(request)
	#print result
	if result== "data":
		#print "Successfully added data to ES"
		return render(request, 'askalma/listing.html')
	else:
		return render(request, 'askalma/question_detail.html')
	#return render(request, 'askalma/question_detail.html', context = context)


def getanswers(request):
	try:
		answer_text= str(request.GET.get("answer_text", ' ')) #getting answer_text
		question_text= str(request.GET.get("question_text", ' '))
		question= es.search(index="questions1", body={"from" : 0, "size" : 1000, "query":{"query_string": {"query": question_text, "default_field": "title"}}})["hits"]["hits"]
		question_id= " "
		user_id= " "
		for q in question:
			question_id= q.get("_id")
		user_profile =_get_user_profile (request.session['email'])
		user_email= user_profile['email']
		user= es.search(index='users', body={"from" : 0, "size": 1000, "query":{ "query_string": {"query": user_email, "default_field": "email"}}})["hits"]["hits"]
		for u in user:
			user_id= u.get("_id")
		doc = {
			"answer_text":answer_text,
			"user_id": user_id,
			"question_id": question_id
		}
		if answer_text!=" ":
			es.index(index='answers', doc_type='answer', body=doc)
		return HttpResponseRedirect("data")
	except KeyError:
		return HttpResponseRedirect("webpage")
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
	strategy.session_set('last_name', details['last_name'])
	#Check if they exist in ES. IF not, add them.
	count = es.search(index='users', body={"size": 0,"query":{ "query_string": { "query": details['email'] , "default_field": 'email' }}})['hits']['total']
	if count == 0:
		doc = {
			"email": details['email'],
			"last_name": details['last_name'],
			"headline" : "Student at Columbia University",
			"profile_pic" : "default.jpg"
		}
		es.index(index="users", doc_type='user', body=doc)

def _get_user_profile (email):
	res = es.search(index='users', body={"from": 0, "size": 1, "query": {
		"query_string": {"query": email, "default_field": 'email'}}})
	#print res
	return res['hits']['hits'][0]['_source']
