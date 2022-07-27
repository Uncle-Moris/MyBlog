from django.urls import path
from .views import register_request

app_name = "register"
urlpatterns = [
    path('register/', register_request, name="register")
]
