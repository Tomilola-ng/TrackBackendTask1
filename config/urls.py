from django.contrib import admin
from django.urls import path
from api.views import get_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_info, name="get_info"),
]
