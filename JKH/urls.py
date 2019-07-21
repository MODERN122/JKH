from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from django.views.generic import TemplateView

from main.views import login_page, logout_page

urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html'), name='main'),
    path('admin/', admin.site.urls),
    path('user_lk/', include('user_lk.urls')),
    path('uk_lk/', include('uk_lk.urls')),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('in_developing/', TemplateView.as_view(template_name='in_developing.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

