from django.urls import path

from Aplikacja import views

app_name = 'Aplikacja'

urlpatterns = [
    path('', views.post_list, name='post_list')
]