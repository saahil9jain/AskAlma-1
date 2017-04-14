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


class QDetailView (generic.DetailView):
    #model = Question
    template_name = "askalma/qdetail.html"

def index(request):
	return render(request, 'askalma/index.html')

#def listing(request):
#	return render(request, 'askalma/listing.html')

def postquestion(request):
	return render(request, 'askalma/post-question.html')
