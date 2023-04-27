from django.urls import path
from .views import *

urlpatterns = [
    path('qr/', qr_gen, name='qr_gen'),
]