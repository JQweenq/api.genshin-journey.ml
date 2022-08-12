from flask import Blueprint
from flask_restful import Api

from app.api.auth import RegistrationRoute, LoginRoute, LogoutRoute
from app.api import (
    characters,
    dictionary,
    meta
)
from app.api.weapons import WeaponsRoute
from app.api.wishes import WishesRoute

api: Blueprint = Blueprint('api', __name__)

api.register_blueprint(characters.route)
api.register_blueprint(dictionary.route)
api.register_blueprint(meta.route)

rest: Api = Api(api)

rest.add_resource(RegistrationRoute, '/register')
rest.add_resource(LoginRoute, '/login')
rest.add_resource(LogoutRoute, '/logout')
rest.add_resource(WishesRoute, '/wishes')
rest.add_resource(WeaponsRoute, '/weapons')
