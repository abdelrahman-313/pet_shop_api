##########################################################
#
# This is a sample flask.cfg for developing a Flask application
#
##########################################################
import os


# Get the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


DEBUG = True

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'pets_db.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False


