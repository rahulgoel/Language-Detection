from django.conf.urls import patterns, include, url
from django.contrib import admin
from manager import LanguageManager

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'langSer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lang_id/', LanguageManager.detect),
)


