from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required		#include decorators
from django.contrib.auth.forms import UserCreationForm

from .forms import ListForm		#Importing
from .models import List		#Connecting with Class that in turn connects to database
from django.shortcuts import redirect
# Create your views here.
#use render
@login_required(login_url='/login/')		#decorator:takes in a function modifies(decorates)it and returns its modified value
def add(request ,*args, **kwargs):
	#An if-else statement can be used with request.user.is_authenticated()
	form = ListForm(request.POST or None, initial={'CONDITION': 'YYYY-MM-DD HH:MM:SS'})		#If it is a post request
	if form.is_valid():
		instance = form.save(commit=False)
		instance.AUTHOR = request.user
		instance.save()
	
	queryset = List.objects.filter(AUTHOR = request.user, NUMBER = request.GET.get('number'))			#Same command can be used in shell
	context = {		
		"object" 	: queryset, 			
		"title"		: "Create",
		"form"		: form  				#Saving all the required HTML in context
	}
	return render(request, 'add.html', context)


def delete(request, task_id):
	List.objects.get(id=task_id).delete()
	print("Here!!!")
	return redirect('../')

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('../')
	else:
		form = UserCreationForm()

	return render(request, 'signup.html', {'form': form})


	

	
