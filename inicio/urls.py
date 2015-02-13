from django.conf.urls import patterns, url

from inicio import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webkufloat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.inicio, name="inicio_redirect"),
    url(r'^inicio/$', views.inicio, name='inicio'),
    url(r'^empresa/$', views.empresa, name='empresa'),
    url(r'^productos/$', views.productos, name='productos'),
    url(r'^clientes_proyectos/$', views.clientes_proyectos, name='clientes_proyectos'),
    url(r'^contacto/$', views.contacto, name='contacto')
)
