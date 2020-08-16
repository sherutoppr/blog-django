from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)                # onetoone relationship between profile and user
    image = models.ImageField(default = 'default.jpeg',upload_to='profile_pics')


    '''
        if u want to rezise or do anything after saving data to model , 
        then make this function, access data , modify them and save them back
        
    '''
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)     # save data before modify

        img = Image.open(self.image.path)    # access image from model

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)             # resize it
            img.save(self.image.path)              # save them back to model





