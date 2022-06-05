"""
WSGI config for ex_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ex_backend.settings')

application = get_wsgi_application()




# custom background thread code

import threading
from swproxy_wrapper.swproxy_wrapper import main as swp_wrapper_main

def threadTask():
    return swp_wrapper_main()

t = threading.Thread(target=threadTask, daemon=True)
t.start()