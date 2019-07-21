from django.urls import path, include
from django.views.generic.list import ListView

from main.models import User
from uk_lk.views import create_user, edit_user, user_list, applications_list, application_page, create_active_work, \
    active_work, vote_list, vote_page, finished_votes, active_works, territories_page, houses_page, flats_page
from uk_lk.views import info_page

urlpatterns = [
    path('user/create/', create_user, name='create_user'),
    path('user/edit/<int:pk>/', edit_user, name='edit_user'),
    path('user/list/', user_list, name='user_list'),
    path('applications/', applications_list, name='applications'),
    path('application/<int:pk>/', application_page, name='application'),
    path('active_work/create/', create_active_work, name='create_active_work'),
    path('active_work/<int:pk>/', active_work, name='active_work'),
    path('active_work/list/', active_works, name='uk_active_works'),
    path('votes/', vote_list, name='votes'),
    path('vote/<int:pk>/', vote_page, name='vote_page'),
    path('votes/finished/', finished_votes, name='uk_finished_votes'),
    path('info/', info_page, name='uk_info_page'),
    path('territories/', territories_page, name='territories'),
    path('<int:pk>/houses/', houses_page, name='houses'),
    path('flats_in_house/<int:pk>/', flats_page, name='flats')
]