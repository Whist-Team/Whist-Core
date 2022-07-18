"""
Retrieves envs for the whist core module.
"""
import os

__version__ = '0.3.0'

ALGORITHM = os.getenv('ALGORITHM', 'HS256')
SECRET_KEY = os.getenv('SECRET_KEY', 'geheim')