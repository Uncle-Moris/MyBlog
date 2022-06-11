from django.urls import path
from .views import posts_list, posts_details

urlpatterns = [
    path('list', posts_list),
    path('<int:post_id>', posts_details)
]