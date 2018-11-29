from flask import Flask
# from config import Config

app = Flask(__name__)
# app.config.from_object(Config)

app.config['SECRET_KEY'] = 'bring-me-thanos'


from app import routes
