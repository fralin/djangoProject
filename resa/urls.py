from django.urls import path, re_path

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from . import views

app_name = 'resa'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Gestion du planning
    path('planning/', views.DiveList.as_view(), name='planning'),

    # Gestion des plongeures
    path('divers/', views.DiverList.as_view(), name='diver_list'),

    ## Gestion des sites
    re_path(r'^site/$', views.SiteList.as_view(), name='site_list'),
    re_path(r'^site/create/$', views.SiteCreate.as_view(), name="site_create"),
    re_path(r'^site/(?P<pk>\d+)/$', views.SiteDetail.as_view(), name="site_detail"),
    re_path(r'^site/(?P<pk>\d+)/update/$', views.SiteUpdate.as_view(), name="site_update"),
    re_path(r'^site/(?P<pk>\d+)/delete/$', views.SiteDelete.as_view(), name="site_delete"),
]