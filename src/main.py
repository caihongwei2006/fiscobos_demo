from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.database.db_manager import init_db
from src.api.routes import register_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agriculture_traceability.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

init_db(db)
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)