# ----------------------
#   Code by Radimich   
#   Date: 2022          
#   Land:Larnevsk     
# ----------------------
from django.urls import path
from . import views

urlpatterns = [
    path('', views.our_publication, name='public-home'),
]