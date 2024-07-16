from flask import Flask, request, session, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
CORS(app,)

db.init_app(app)
migrate = Migrate(app=app, db=db)

@app.route('/')
def hello():
    return f'Hello there!'

if __name__ == '__main__':
    app.run(port=5555, debug=True)