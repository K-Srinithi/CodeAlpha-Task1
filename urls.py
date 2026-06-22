from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Add this
from django.conf.urls.static import static # Add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

# Idhai file-oda kadasiya add pannunga
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)