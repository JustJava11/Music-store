from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='username')
    bio = models.TextField(null=True ,blank=True, verbose_name='description')
    avatar = models.ImageField(upload_to='images/account_avatars/', default='images/account_avatars/default.jpg', blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='registration_date')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'profiles'

