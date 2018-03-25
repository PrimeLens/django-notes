from django.conf.urls import include, url
from django.contrib import admin

from streams import views 

urlpatterns = [
    # Examples:
    # url(r'^$', 'testsoc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
