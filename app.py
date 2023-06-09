from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    name = db.Column(db.String(255))

    def __init__(self, username, name):
        self.username = username
        self.name = name


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = User(request.form['username'], request.form['name'])
        db.session.add(user)
        db.session.commit()
        return redirect('/') 
    
    usernames = User.query.all()
    return render_template('index.html', usernames=usernames)

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit() 
    return redirect('/') 

if __name__ == '__main__':
    app.run(debug=True)


