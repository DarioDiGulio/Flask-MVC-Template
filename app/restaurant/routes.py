from flask.ext.via.routers import default
from views import *

routes = [
    default.Functional('/restaurant', profile),
    default.Functional('/restaurant/upload', upload)
]