
from django.urls import path , include
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', views.register , name='home'),
    path('home', views.register),
    path('eadd', views.eadd , name='eadd'),
    path('eremauth/<int:pk>', views.eremauth , name='eremauth'),
    path('eremove/<int:pk>', views.eremove, name='eremove'),
    path('eview', views.eview, name='eview'),
	path('laddentity', views.laddentity , name='laddentity'),
    path('ladd', views.ladd , name='ladd'),
    path('lview', views.lview , name='lview'),
    path('dadd', views.dadd , name='dadd'),
    path('dremove/<int:pk>', views.dremove , name='dremove'),
    path('dremauth/<int:pk>', views.dremauth , name='dremauth'),
    path('dview', views.dview , name='dview'),
    path('login', views.login , name='login'),
    path('pics/' , views.img  , name='iview'),
    path('profile/<int:pk>', profile.as_view(), name='profile'),
    path('liview', views.liview, name='liview'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('lview1', lview1.as_view(), name='lview1'),
    path('liview1/<int:pk>', liview1.as_view(), name= 'liview1'),
    # path('', views.),
    # path('', views.),
    # path('', views.),
    # path('', views.),
    # path('', views.),
    # path('', views.),
    # path('', views.),
]
