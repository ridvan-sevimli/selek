from django.urls import path

from . import views

app_name = "fahrschule"
urlpatterns = [
    path("", views.index, name="index"),
]