#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/ShoprClone/")

from app import app as application
application.secret_ket = 'ffdd55e74cc7a0e0018a59f80df52991'
