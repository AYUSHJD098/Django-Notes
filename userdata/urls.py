from django.urls import path
from userdata import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createnote', views.create_note, name='create_note'),
    path('viewnote/<str:pk>', views.view_note, name='view_note'),
    path('updatenote/<str:pk>', views.update_note, name='update_note'),
]
