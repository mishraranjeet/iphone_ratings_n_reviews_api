
from django.contrib import admin
from django.urls import path
from iphone_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('api/', api_view,name='api_view'),
]
