# app.py
from flask import Flask
from models.user import db
from routes.user_routes import user_bp
# import os

# os.system('cls')


app = Flask(__name__)
app.secret_key = 'siteapp123'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

db.init_app(app)

with app.app_context():
    db.create_all()  # Cria as tabelas no banco de dados

app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
 