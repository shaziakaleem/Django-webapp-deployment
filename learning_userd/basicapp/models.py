from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    profile_pics = models.ImageField(upload_to='basic_app/profile_pics',blank = True)
    portfolio_site = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
