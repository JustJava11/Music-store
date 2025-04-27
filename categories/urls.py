from django.urls import path
from categories.views import *

urlpatterns = [
    path('create/', CreateCategoryView.as_view(), name='category_create'),
    path('list/', ListCategoryView.as_view(), name='category_list'),
]