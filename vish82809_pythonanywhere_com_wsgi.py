import os
import sys

# assuming your Django settings file is at
# '/home/myusername/mysite/mysite/settings.py'
path = '/home/vish82809/The-Royal'
if path not in sys.path:
     sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'vehicleservicemanagement.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()