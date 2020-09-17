"""
WSGI config for cocus_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

"""

import os
from dj_static import Cling

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cocus_project.settings')

application = Cling(get_wsgi_application())
