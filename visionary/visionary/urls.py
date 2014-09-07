from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

# may be unnecessary
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'visionary.views.home', name='home'),
    # url(r'^blog/', ),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('forum.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# may be unnecessary
urlpatterns += staticfiles_urlpatterns()
