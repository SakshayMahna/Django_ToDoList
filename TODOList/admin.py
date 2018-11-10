from django.contrib import admin
from .models import List		#.localrefrencing
# Register your models here.
#Customising admin page of List

class ListAdminModel(admin.ModelAdmin):
	list_display = ["AUTHOR","MEMO", "CONDITION", "NUMBER"]		
	class Meta:						#Overriding parent-class
		model = List


admin.site.register(List, ListAdminModel)		#Don't forget to makemigrations		#built in function to register
