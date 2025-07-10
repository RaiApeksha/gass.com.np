import os
import sys

# 1) Add your application root to the Python path
sys.path.insert(0, '/home2/gassadmin/GASSPRO')

# 2) Activate the virtual environment
activate_this = '/home2/gassadmin/virtualenv/GASSPRO/3.11/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# 3) Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gass.settings')

# 4) Get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
