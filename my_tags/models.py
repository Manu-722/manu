# from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
 title = models.CharField(max_length=255)
 author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
 text = models.TextField()
 created_date = models.DateTimeField(auto_now_add=True)
 published_date = models.DateTimeField(blank=True, null=True)
 is_active = models.BooleanField(default=True)

 def __str__(self):
	 return self.title
 
class Editor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='editors') #sets up a foreign key relationship.On delete if the related blog is deleted the editpr is also deleted.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
