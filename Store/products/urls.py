from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #url(r'^$', views.samplemethod, name='samplemethod'),
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^addproducts/$', views.addproducts, name='addproducts'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
]

