from django.urls import path
from .import views
# imports views.py

urlpatterns =[
    path("", views.home,name="home")
    # an empty path  means to default to the root
]