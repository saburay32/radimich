from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews
from users import views as userViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', userViews.register, name='reg'),
    path('profile/', userViews.profile, name='profile'),
    path('', include('blog.urls')),
    path('user/', authViews.LoginView.as_view(template_name = 'users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name = 'users/exit.html'), name='exit'),
    path('our-public', include('our_public.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)