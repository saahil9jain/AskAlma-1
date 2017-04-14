from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# class User (models.Model):
#     email = models.CharField(max_length=32)
#     firstname = models.CharField(max_length=64)
#     lastname = models.CharField(max_length=64)

#     def __str__(self):
#         return self.firstname + " " + self.lastname

#     def get_absolute_url (self):
#         return reverse("askalma:qdetail" , kwargs={'pk':self.pk} )


# class Question (models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_anonymous =  models.BooleanField ()
#     title = models.CharField (max_length=128)
#     body = models.TextField()


#     def __str__(self):
#         return self.user.firstname + " " +  self.user.lastname + " - " + self.title

#GUYS: username: admin password: askalma123
