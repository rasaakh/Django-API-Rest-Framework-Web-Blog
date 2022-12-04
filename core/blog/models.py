from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils.translation import ugettext
from django.db import models

# getting user model object
User = get_user_model()

class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default="blog/default.jpg" )
    author = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags =TaggableManager() 
    category = models.ManyToManyField('Category', blank=True)
    counted_view= models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    login_required=models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['title']
       

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
