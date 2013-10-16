#/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

path = '/home/zarik/web/usadba/django_usadba'
if path not in sys.path:
    sys.path.append(path)



os.environ['DJANGO_SETTINGS_MODULE'] = 'usadba.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


