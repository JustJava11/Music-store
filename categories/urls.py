from django.urls import path
from categories.views import *

urlpatterns = [
    path('list/', ListCategoryView.as_view(), name='category_list'),
    path('detail/<int:pk>', DetailCategoryView.as_view(), name='category_detail'),
]
