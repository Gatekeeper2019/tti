from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
   path('', views.index, name='index'),
   path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('dash/', views.dash, name='dash'),
   path('field_office/', views.field_office, name='field_office'),
   path('showpaul/', views.showpaul, name='showpaul'),
   path('paulapplication/', views.paulapplication, name='paulapplication'),


]
