from django.http import HttpResponseRedirect
from django.views import generic
from .models import *
from django.shortcuts import render
import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch("search-askalma-ec4hakudbwu54iw5gnp6k6ggpy.us-east-1.es.amazonaws.com", port=443,
				   use_ssl='true')


def _isLoggedIn(request):
	try:
		user_id = request.session['user_id']
		last_in = request.session['last_in']
		if (last_in-datetime.datetime > 30000):
			return HttpResponseRedirect(reverse('social:begin' ,args=('google-oauth2',)))
		return None
	except KeyError:
		return HttpResponseRedirect(reverse('social:begin' ,args=('google-oauth2',)))


def index(request):
	#result = _isLoggedIn(request)
	#if result != None: return result
	return render(request, 'askalma/index.html')

class QDetailView (generic.DetailView):
    template_name = "askalma/qdetail.html"

def listing(request):
	return render(request, 'askalma/listing.html')

def postquestion(request):
	return render(request, 'askalma/post-question.html')

def profile (request):
	'''doc = {
		"userid" : 'hj2441',
		"firstname" : 'Hamza'
		, "lastname" : "Jazmati"
	}
	es.index('users','user', body=doc)'''
	#user_id = "hj2441"
	#result = es.search(index='users', body={"form" : 0 , "size" : 1 , "query": {"query_string" : { "query": user_id , "default_field": 'userid' }}})['hits']['hits'][0]

	return render(request, 'askalma/profile.html')

def edit_profile (request , user_id ):
	#_isLoggedIn(request)
	if (request.session['user_id'] !=  user_id):
		render(request, 'askalma/404.html')
	else:
		render(request , 'askalma/profile-setting.html')

def logout(request):
	try:
		del request.session['user_id']
	except:
		pass
	return index(request)

def contactus (request):
	pass

def result (request):
	#GET Token, ask for email , first name, last name.
	#Check if they exist in ES. IF not, add them.
	# add them to the session either way:
	# request.session['user_id'] = "hj2441@columbai.edu"
	#last_in = datetime.datetime
	return index(request)

def qdetail(request):
	return render(request, 'askalma/question_detail.html')
