from django.urls import path
from . import views

app_name = 'accounts'  # This is the namespace for your app's urls

urlpatterns = [
    path('accounts/signup', views.signup, name='accounts'),  # The signup view
]
