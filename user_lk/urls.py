from django.urls import path, include
from user_lk.views import info_page, applications_list, create_application, application_page, create_vote, vote_page, \
    vote_list, active_works_list, user_edit, finished_votes

urlpatterns = [
    path('info/', info_page, name='info_page'),
    path('applications/', applications_list, name='applications_list'),
    path('applications/create', create_application, name='create_application'),
    path('application/<int:pk>/', application_page, name='application_page'),
    path('vote/create/', create_vote, name='create_vote'),
    path('vote/<int:pk>/', vote_page, name='user_vote_page'),
    path('votes/active/', vote_list, name='active_votes'),
    path('votes/finished/', finished_votes, name='finished_votes'),
    path('active_works/', active_works_list, name='active_works'),
    path('user_edit/', user_edit, name='user_edit'),
]