from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'visionary.views.home', name='home'),
    # url(r'^blog/', ),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('forum.urls')),
]
