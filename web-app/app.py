from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3
import os

# specify directory where db is
# currentdirectory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recommendations_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Clothing = db.Table('strict_filtering', db.metadata, autoload=True, autoload_with = db.engine)
Base = automap_base()
Base.prepare(db.engine, reflect=True)
Clothing = Base.classes.strict_filtering #name of table


@app.route("/")
def main():
    new_product = Product(name="New Product")
    # results = db.session.query(Clothing).all()
    # for r in results:
    #     print(r.article_id)
    return ''

# @app.route("/recommended", methods=["POST"])
# def recommended():
#     if request.method=="POST":
#         gender=request.form.get("gender")
#         product_appearance=request.form.get("product_appearance")
#         Sample = 
#         return(render_template("index.html"))

if __name__ == "__main__":
    app.run()
    
    
    
# connection = sqlite3.connect(currentdirectory + "\ recommendations_database.db")
# cursor = connection.cursor() 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recommendations_database.db'
# db = SQLAlchemy(app)
# db.Model.metadata.reflect(db.engine)
# class Clothes(db.Model):
#     __table__ = db.Model.metadata.tables["strict_filtering"]
#     def __repr__(self):
#         return self.DISTRICT