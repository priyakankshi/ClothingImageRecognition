from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3
import os

app = Flask(__name__)

# specify directory where db is
# currentdirectory = os.path.dirname(os.path.abspath(__file__))
# db_name = currentdirectory + "/ recommendations_database.db"
db_name = 'recommendations_database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# Clothing = db.Table('strict_filtering', db.metadata, autoload=True, autoload_with = db.engine)
Base = automap_base()
Base.prepare(db.engine, reflect=True)
Clothing = Base.classes.strict_filtering #name of table

# class Inventory(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

# For testing whether sql connection works
# @app.route('/')
# def testdb():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text

@app.route('/', methods=["GET", "POST"])
def main():
    try:
        result = db.session.query(Clothing).filter_by(graphical_appearance_name = 'chambray').all()
        for r in result:
            print(r.article_id)
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
# connection = sqlite3.connect(currentdirectory + "/ recommendations_database.db")
# cursor = connection.cursor() 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recommendations_database.db'
# db = SQLAlchemy(app)
# db.Model.metadata.reflect(db.engine)
# class Clothes(db.Model):
#     __table__ = db.Model.metadata.tables["strict_filtering"]
#     def __repr__(self):
#         return self.DISTRICT