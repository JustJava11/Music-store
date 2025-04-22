from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls'))
]
