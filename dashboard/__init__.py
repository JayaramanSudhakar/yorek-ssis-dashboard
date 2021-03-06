"""
The flask application package.
"""

from dashboard import config
from flask import Flask
import os

app = Flask(__name__)

app.config.from_object(config)

envConfig = 'DASHBOARD_CONFIG'
fileConfig = 'config.cfg'

envConfigExists = os.getenv(envConfig) != None
fileConfigExists = os.path.isfile('config.cfg')

# If no configuration specific via environment variable
# use the local configuration file, if that exists
if envConfigExists == False and fileConfigExists == True:
    os.environ[envConfig] = os.path.join('..','','') + fileConfig
    envConfigExists = True

# Load the configuration file specified in the environment variable
if envConfigExists == True:
    print("Loading configuration from: " + envConfig + " > " + os.environ[envConfig])
    app.config.from_envvar(envConfig)

from dashboard.views import *
from dashboard.processors import *
from dashboard.filters import *