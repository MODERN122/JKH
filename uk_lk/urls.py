from django.urls import path, include
from user_lk.views import info_page

urlpatterns = [
    path('info/', info_page, name='info_page'),
]