from flask import Flask, request, session, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db
from config import Config
from auth import auth_bp, bcrypt, jwt
from commodities import commodities_bp


app = Flask(__name__)
app.config.from_object(Config)
app.json.compact = False

app.register_blueprint(auth_bp)
app.register_blueprint(commodities_bp)
CORS(app,)



bcrypt.init_app(app)
db.init_app(app)
jwt.init_app(app)
migrate = Migrate(app=app, db=db)


@app.route('/')
def hello():
    return f'Hello there!'

if __name__ == '__main__':
    app.run(port=5555, debug=True)