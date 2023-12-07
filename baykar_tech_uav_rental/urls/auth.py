from django.urls import path
from ..views import auth

urlpatterns = [
    path('sign-up', auth.sign_up, name='sign_up'),
]
