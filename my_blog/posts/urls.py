from django.urls import path
from .views import  posts_list, posts_details

urlpatterns = [
    path('list', posts_list),
    path('details', posts_details)
]