import os
from pickle import FALSE

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEM_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postresql://postgres:toor00@localhost/postgres"