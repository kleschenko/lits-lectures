from flask import Flask, flash, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('my_app')
app.config['SECRET_KEY'] = 'my_top_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models, views

if __name__ == "__main__":
    app.run()
