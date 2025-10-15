from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
   path("<str:item>",views.course, name='course'),#dynamic routing
   path("multiply/<int:a>/<int:b>", views.multiply_view, name='multiply'), #dynamic routing with integers
   
]

