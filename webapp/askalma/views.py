from django.views import generic
from .models import *
from django.views.generic import CreateView , UpdateView , DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
import datetime

def _isLoggedIn(request):
	try:
		userid = request.session['userid']
		lastin = request.session['lastin']
		if (lastin-datetime.time > 30000):
			print "Not Logged In"
			return
		_oauth(request)
	except KeyError:
		print "NOT LOGGED IN"
		return

def _oauth(request):
	#Please add your authentication process here.
	return


def index(request):
	_isLoggedIn(request)
	return render(request, 'askalma/index.html')


class QDetailView (generic.DetailView):
    #model = Question
    template_name = "askalma/qdetail.html"

#def listing(request):
#	return render(request, 'askalma/listing.html')
def postquestion(request):
	return render(request, 'askalma/post-question.html')
