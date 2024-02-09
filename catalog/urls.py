from django.urls import path
from catalog.views import contacts, homepage


urlpatterns = [
    path('', homepage),
    path('contacts/', contacts),
]
