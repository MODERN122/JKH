from django.urls import path, include
from user_lk.views import info_page, applications_list, create_application, application_page

urlpatterns = [
    path('info/', info_page, name='info_page'),
    path('applications/', applications_list, name='applications_list'),
    path('applications/create', create_application, name='create_application'),
    path('application/<int:pk>/', application_page, name='application_page'),
]