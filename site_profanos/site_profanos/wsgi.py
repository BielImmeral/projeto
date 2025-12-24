import os
import sys

path = '/home/seu_usuario/site_profanos'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'site_profanos.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
