from django.db import models
from django.contrib.auth.models import User   			#To associate user with a model
# Create your models here.
#MVC: Model View Controller

class UserData(models.Model):
	AUTHOR = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)    #on_delete=CASCADE means delete every reference	
	class Meta:												#Since editable=False we have to manually set its value in views
		abstract=True

"""
Abstract base classes are useful when you want to put some common 
information into a number of other models. You write your base class
and put abstract=True in the Meta class. This model will then not 
be used to create any database table. Instead, when it is used as a
base class for other models, its fields will be added to those of the 
child class.
"""

class List(UserData):			#You have to register this on admin site too	
	MEMO    	=	models.CharField(max_length=120)
	CONDITION	=	models.DateTimeField()
	CHOICES     = (
		(1, 'One'),
		(2, 'Two'),
		(3, 'Three'),
		(4, 'Four'),
	)
	NUMBER      =   models.IntegerField(choices=CHOICES, default=1)
	
	def __str__(self):			#To set title
		return self.MEMO




#YAY!!!It's working!!!!!

"""
The HTTP Methods
CREATE - POST
RETREIVE - GET
UPDATE - PUT/PATCH
DELETE - DELETE
"""


"""		An advanced method
class UserDataForm(models.ModelForm):
                         
    # Overriding save allows us to add the user from the request    
    def save(self, user, commit=True):
        # get the instance so we can add the user to it.
        instance = super(UserDataForm, self).save(commit=False)  #super function allows to use function from original function which has been overridden
        instance.user = user
 
        # Do we need to save all changes now?
        if commit:
            instance.save()
            self.save_m2m()
 
        return instance
 
class PostForm(UserDataForm):
    class Meta:
        model = Post
 
# in your view
def save_post(request):
     post_form = PostForm(request.POST)
     post_form.save(user=request.user)
"""