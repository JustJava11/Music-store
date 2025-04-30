from django.urls import path
from profiles.views import *

urlpatterns = [
    path('profile/<int:pk>', profile_detail, name='profile'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('update-user/', update_user, name='update_user'),
    path('update/', update_profile, name='update_profile'),
]
