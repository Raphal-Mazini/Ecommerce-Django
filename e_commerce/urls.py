from django.urls import include, path
from django.contrib import admin
from .views import home_page

urlpatterns = [
        path('', home_page),
        path('admin/', admin.site.urls),
]
