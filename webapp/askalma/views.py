from django.views import generic
from .models import *
from django.views.generic import CreateView , UpdateView , DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from django.shortcuts import render
import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch("search-askalma-ec4hakudbwu54iw5gnp6k6ggpy.us-east-1.es.amazonaws.com", port=443,
				   use_ssl='true')


def _isLoggedIn(request):
	try:
		user_id = request.session['user_id']
		last_in = request.session['last_in']
		if (last_in-datetime.time > 30000):
			print("Not Logged In")
			return
		_oauth(request)
	except KeyError:
		print("NOT LOGGED IN")
		return

def _oauth(request):
	#Please add your authentication process here.
	return


def index(request):
	_isLoggedIn(request)
	return render(request, 'askalma/index.html')

class QDetailView (generic.DetailView):
    template_name = "askalma/qdetail.html"

def listing(request):
	return render(request, 'askalma/listing.html')

def postquestion(request):
	return render(request, 'askalma/post-question.html')

def profile (request, user_id):
	#GET DATA FROM ES.
	return render(request, 'askalma/profile.html')

def edit_profile (request , user_id):
	_isLoggedIn(request)
	if (request.session['user_id'] !=  user_id):
		render(request, 'askalma/404.html')
	else:
		render(request , 'askalma/profile-setting.html')

def logout(request):
	del request.session['user_id']
	index(request)