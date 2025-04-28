from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='username')
    description = models.TextField(null=True ,blank=True, verbose_name='description')
    avatar = models.ImageField(upload_to='media/images/account_avatars/', default='account_avatars/default.jpg', blank=True, null=True)
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='registration_date')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'profiles'

