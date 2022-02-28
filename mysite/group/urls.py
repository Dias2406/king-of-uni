from django.urls import path
from . import views


urlpatterns = [
    path('', views.group, name='group-home'),
    path('join_group.html', views.group, name='join_group'),

]

