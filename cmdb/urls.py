from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.user_login),
    url(r'^index/',views.index),
]
