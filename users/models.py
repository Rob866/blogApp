from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Perfil'

    def save(self,**kwargs):
        super().save() 
        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            outputsize=(300,300)
            img.thumbnail(outputsize)
            img.save(self.image.path)




     
 