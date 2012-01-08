from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'main.views.index'),
  url(r'^new_board$', 'main.views.new_board'),
  url(r'^get_boards$', 'main.views.get_boards'),
  url(r'^show_board/(?P<id>\d+)', 'main.views.show_board'),
)
