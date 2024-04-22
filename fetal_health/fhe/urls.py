from django.urls import path, include
from fhe.views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
]