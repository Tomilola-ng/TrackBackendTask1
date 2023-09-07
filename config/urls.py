from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static  import static
from api.views import get_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_info, name="get_info"),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
