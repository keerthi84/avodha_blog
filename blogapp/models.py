from django.db import models
from django.urls import reverse
import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class blog(models.Model):

    title=models.CharField(max_length=50)
    title_tag=models.CharField(max_length=225)
    # author_use= models.ForeignKey(User,on_delete=models.CASCADE)
    author=models.CharField(max_length=50)
    date = models.DateField(default=datetime.date.today)
    img=models.ImageField(upload_to='images')
    # body=models.TextField()
    body=RichTextField(blank=True,null=True)


    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return reverse('home')


