# pages/urls.py

from pages.views import home
from django.urls import path

urlpatterns = [
path('', home, name = 'home')
]