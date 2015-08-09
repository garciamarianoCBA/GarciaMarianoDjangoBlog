from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'HTML.views.home', name='home'),  
                       url(r'^$', 'HTML.views.cv', name='cv'),
                       url(r'^calc/$', 'HTML.views.calc', name='calc'),                      
                       url(r'^conv/$', 'HTML.views.conv', name='comv'),                      
                       url(r'^cron/$', 'HTML.views.cron', name='cron'),                      
)
