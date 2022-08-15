from flask_migrate import Migrate
from run import app
from app.models.utils import db

migrate = Migrate(app, db)
