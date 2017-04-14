from django.conf.urls import url
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'askalma'
urlpatterns = [
url(r'^$', views.index, name='index'),
#url(r'listing', views.listing, name='listing'),
url(r'post-question', views.postquestion, name='post-question'),
]
