from django.views import generic
from .models import *
from django.views.generic import CreateView , UpdateView , DeleteView
from django.core.urlresolvers import reverse_lazy


class QDetailView (generic.DetailView):
    model = Question
    template_name = "askalma/qdetail.html"
