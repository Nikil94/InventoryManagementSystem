from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #url(r'^$', views.samplemethod, name='samplemethod'),
    url(r'^home/$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^addproducts/$', views.addproducts, name='addproducts'),
    url(r'^viewproducts/$', views.viewproducts, name='viewproducts'),
    url(r'^deleteproduct/(?P<id>\d+)/$', views.deleteproduct, name='deleteproduct'),
    url(r'^updateproductstatus/(?P<id>\d+)/$', views.updateproductstatus, name='updateproductstatus'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
]

