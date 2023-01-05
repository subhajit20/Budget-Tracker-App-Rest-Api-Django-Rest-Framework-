from django.urls import path

from .views import Register,Login

urlpatterns = [
    path("u1/", Register),
    path("l1/", Login),
]