#!/usr/bin/python2
# coding: utf-8
from django.conf.urls.defaults import *

urlpatterns = patterns('main.views',

    url(r'^page/(?P<alias>\w+)/$', 'show', None, name='page_link'),
    url(ur'^ферма/новости$', 'show', {'alias':'mainpage'}, name='url_news'),
    url(ur'^ферма/продукты$', 'show', None, name='url_products'),
    url(ur'^доставка$', 'show', None, name='url_delivery'),
    url(ur'^рецепты$', 'show', None, name='url_recipes'),
    url(ur'^отзывы$', 'show', None, name='url_testimonials'),
    url(ur'^контакты$', 'show', None, name='url_contact'),
   
)
