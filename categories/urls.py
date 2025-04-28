from django.urls import path
from categories.views import *

urlpatterns = [
    path('create/', CreateCategoryView.as_view(), name='category_create'),
    path('update/<int:pk>', UpdateCategoryView.as_view(), name='category_update'),
    path('delete/<int:pk>', DeleteCategoryView.as_view(), name='category_delete'),

    path('list/', ListCategoryView.as_view(), name='category_list'),
    path('detail/<int:pk>', DetailCategoryView.as_view(), name='category_detail'),
]
