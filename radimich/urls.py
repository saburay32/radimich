from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('user/',authViews.LoginView.as_view(),name='auth'),
    path('exit/',authViews.LogoutView.as_view(),name='exit'),
    path('our-public', include('our_public.urls')),
]
