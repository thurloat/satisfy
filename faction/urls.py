from django.conf.urls.defaults import *

urlpatterns = patterns('faction.views',
    url(r'overview/$',                      'overview',             name='faction-overview'),
    url(r'companies/$',                     'company_list',         name='faction-company-list'),
    url(r'register/$',                      'register_company',     name='faction-register'),
    url(r'company/(?P<company_slug>.+)/$',  'company_dashboard',    name='faction-company-dashboard'),
    url(r'company/(?P<company_slug>.+)/topics/$', 'company_topics',  name='faction-company-topics'),
)