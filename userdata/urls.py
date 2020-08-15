from django.urls import path
from userdata import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createnote', views.create_note, name='create_note'),
]
