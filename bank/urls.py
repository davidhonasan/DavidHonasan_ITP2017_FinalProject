from django.conf.urls import url
from . import views

app_name = 'bank' #app name for namespace

urlpatterns = [
    url(r'^$', views.index, name='main'),   # main page
    url(r'^login/$', views.login_form, name='login_form'),  # login page
    url(r'^login/login$', views.login_action, name='login'),    # login action
    url(r'^logout/$', views.logout_action, name='logout'),  # logout action
    url(r'^menu/$', views.menu, name="menu"),   # menu
    url(r'^menu/balance/$', views.balance, name="balance"), # balance
    url(r'^menu/transfer/$', views.transfer_form, name="transfer_form"),# transfer page
    url(r'^menu/transfer/transfer/$', views.transfer, name='transfer'), # transfer action
]
