"""
Retrieves envs for the whist core module.
"""
import os

# remember to also update the version in pyproject.toml!
__version__ = '0.8.0'

ALGORITHM = os.getenv('ALGORITHM', 'HS256')
SECRET_KEY = os.getenv('SECRET_KEY', 'geheim')
