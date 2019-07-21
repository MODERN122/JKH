from django.urls import path, include
from django.views.generic.list import ListView

from main.models import User
from uk_lk.views import create_user, edit_user, user_list, applications_list, application_page, create_active_work, \
    active_work, vote_list
from user_lk.views import info_page

urlpatterns = [
    path('user/create/', create_user, name='create_user'),
    path('user/edit/<int:pk>/', edit_user, name='edit_user'),
    path('user/list/', user_list, name='user_list'),
    path('applications/', applications_list, name='applications'),
    path('application/<int:pk>/', application_page, name='application'),
    path('active_work/create/', create_active_work, name='create_active_work'),
    path('active_work/<int:pk>/', active_work, name='active_work'),
    path('votes/', vote_list, name='votes'),
]