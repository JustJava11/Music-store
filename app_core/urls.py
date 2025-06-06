from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page_app.urls')),
    path('profiles/', include('profiles.urls')),
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
