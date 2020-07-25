from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("natwit", views.natwit, name="natwit"),
    path("yodyiam", views.yodyiam, name="yodyiam"),
    path("<str:name>", views.greet, name="greet")

]
