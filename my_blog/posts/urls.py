from django.urls import path
from .views import Offer_1, Offer_2, Offer_3

urlpatterns = [
    path('offer_1', Offer_1),
    path('offer_2', Offer_2),
    path('offer_3', Offer_3)
]