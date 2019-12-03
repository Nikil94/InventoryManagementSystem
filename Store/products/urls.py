from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from . views  import *

urlpatterns = [
    #url(r'^$', views.samplemethod, name='samplemethod'),
    url(r'^home/$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^addproducts/$', views.addproducts, name='addproducts'),
    url(r'^viewproducts/$', views.viewproducts, name='viewproducts'),
    url(r'^search/$', views.search, name='search'),
    url(r'^deleteproduct/(?P<id>\d+)/$', views.deleteproduct, name='deleteproduct'),
    url(r'^updateproductstatus/(?P<id>\d+)/$', views.updateproductstatus, name='updateproductstatus'),
    url(r'^productsview/$', views.productsview.as_view(), name='productsview'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^allproducts/', views.allproducts.as_view(), name="allproducts"),
    #url(r'productsview/<int:id>/', views.Productsview.as_view(), name="productsview"),
    #url(r'^productsview/(?P<pid>\w+)/$', views.productsview.as_view(), name="productsview"),
]



#urlpatterns += staticfiles_urlpatterns()