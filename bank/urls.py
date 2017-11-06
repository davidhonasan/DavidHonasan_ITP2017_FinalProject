from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'bank'

urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^login/$', views.login_form, name='login_form'),
    url(r'^login/login$', views.login_action, name='login'),
    url(r'^logout/$', views.logout_action, name='logout'),
    url(r'^menu/$', views.menu, name="menu"),
    url(r'^menu/balance/$', views.balance, name="balance"),
    url(r'^menu/transfer/$', views.transfer_form, name="transfer_form"),
    url(r'^menu/transfer/transfer/$', views.transfer, name='transfer'),
]
