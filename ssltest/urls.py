from django.urls import path
from .views import *

urlpatterns = [
    path('', sslview, name='home'),

]