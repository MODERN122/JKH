from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import login_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_lk/', include('user_lk.urls')),
    path('uk_lk/', include('uk_lk.urls')),
    path('login/', login_page, name='login_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

