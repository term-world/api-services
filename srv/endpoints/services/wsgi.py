"""
WSGI config for services project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

# application = get_wsgi_application()

# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '../../libs'))

import os
import sys
from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD:services/src/api/api/wsgi.py
# Add the path to term-util/libs to the Python path
sys.path.append('/Users/bergasanargya/summer_research_AC/term-util/libs')
print("Python path in wsgi.py:")
for path in sys.path:
    print(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'services.settings')
>>>>>>> main:srv/endpoints/services/wsgi.py

application = get_wsgi_application()




