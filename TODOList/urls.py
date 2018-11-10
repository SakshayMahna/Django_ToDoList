#Made to remove conflicts...
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    re_path(r"^delete/(?P<task_id>\d+)$", views.delete, name='delete'),		#Captures the text matched by "regex" into the group "name".
    path('', views.add),
    path('signup', views.signup, name="signup"),
]	#Obsolete version of re_path