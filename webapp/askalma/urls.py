from django.conf.urls import url
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'askalma'

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^index$', views.index, name='index'),
url(r'^listing', views.listing, name='listing'),
url(r'^post-question', views.postquestion, name='post_question'),
url(r'^profile/$', views.profile, name='profile'),
url(r'^editprofile/(?P<user_id>[a-zA_Z0-9]+)/$', views.edit_profile ,name='edit_profile'),
url(r'^logout$', views.logout ,name='logout'),
url(r'^contactus$' , views.contactus , name="contactus"),
url(r'^result' , views.result , name="result")
]
