from django.conf.urls import url
from . import views

app_name = 'askalma'
urlpatterns = [
url(r'^askalma', 'templates/index.html'),
]
