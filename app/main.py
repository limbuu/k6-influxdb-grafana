from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

# create flask app
app = Flask(__name__)
server_port=5000
host_address="0.0.0.0"
# configuraton
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
# create object of Sqlalchemy class with app object as parameter
db = SQLAlchemy(app)

# user model
class User(db.Model):

    id = db.Column(db.Integer, primary_key = True) 
    public_id = db.Column(db.String(50), unique = True) 
    name = db.Column(db.String(100)) 
    email = db.Column(db.String(70), unique = True) 
    password = db.Column(db.String(80)) 

# @app.route('/user/{userid}',methods=['PATCH'])
# def update_user():

# @app.route('/user/{userid}',methods=['GET'])
# def get_user():

# @app.route('/user',methods=['GET'])
# def get_all_users():

# @app.route('/logout',methods=['POST'])
# def logout():

# @app.route('/login',methods=['POST'])
# def login():

@app.route('/register', methods=['POST'])
def register():
    # convert form data to dictionary
    data = request.form
    # get name, email and password
    name, email, password = data.get('name'), data.get('email'), data.get('password')

    user = User( 
            public_id = str(uuid.uuid4()), 
            name = name, 
            email = email, 
            password = generate_password_hash(password) 
        ) 
    db_email = 
    if email == db_email :
        return "User is already created"
    else:
        # insert user 
        db.session.add(user) 
        db.session.commit() 
        return "User sucessfully created"

if __name__=="__main__":
    db.create_all()
    app.run(host=host_address,port=server_port,debug=True)
    
