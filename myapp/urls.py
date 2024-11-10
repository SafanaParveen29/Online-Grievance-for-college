
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('edit_users/<int:id>/',views.edit_users,name='edit_users'),
    path('clgComp/',views.clgComp,name='clgComp'),
    path('hosComp/',views.hosComp,name='hosComp'),
    path('cons/',views.cons,name='cons'),
    path('creti/',views.creti,name='creti'),
    path('vcollege/',views.vcollege,name='vcollege'),
    path('vhostel/',views.vhostel,name='vhostel'),
    path('vcons/',views.vcons,name='vcons'),
    path('vcerti/',views.vcerti,name='vcerti'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('edit_users/',views.edit_users,name='edit_users'),
    path('staff_login/',views.staff_login,name='staff_login'),
    path('staff_logout/',views.staff_logout,name='staff_logout'),
    path('dclg/',views.dclg,name='dclg'),
    path('dhos/',views.dhos,name='dhos'),
    path('dcons/',views.dcons,name='dcons'),
    path('dcerti/',views.dcerti,name='dcerti'),
    
]
