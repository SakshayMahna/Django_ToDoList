"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf   			#Following this
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
#Watch this website...
from django.contrib import admin
from django.urls import path, include, re_path
from TODOList import views

urlpatterns = [
    path('admin/', admin.site.urls), 			#Here address can be added in "" conncected using .
    path('', include('TODOList.urls')),
    re_path(r"^delete/(?P<task_id>\d+)$", views.delete, name='delete'),
    path('', include('django.contrib.auth.urls')),		#Type the exact same address in browser and see magic
    re_path(r'',include('allauth.urls')),     #To redirect
]				#One more magic: just write this and store login logout password etc page in template/registration
				#Will automatically render the pages

"""
Format settings.py, use in html, edit admin settings, configure the api
"""