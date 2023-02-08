# am importing the needed classes from flask
from flask import Blueprint, redirect, render_template, url_for,request, flash
# am importing UserMixin from flask_login. not in use yet
from flask_login import UserMixin
# importing my password hasher. You will need to install this package with pip3
from werkzeug.security import generate_password_hash,check_password_hash
# importing database from app_connector
from app_connector import db
# also importing  the User class(table). that is what makes a user a user🤣
from database.db_schema import Admin

# making blueprint for routing  
auth =  Blueprint("auth",__name__)        

# using blueprint to route 
@auth.route("/register",methods=["GET","POST"])
def register():
    # checking the request type
    if request.method == "POST":
        # Collecting and storing the data from the frontend
        name = request.form.get("firstname")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        # checking if the database to see if the email already exist
        user = Admin.query.filter_by(email=email).first()
        if user:
            # showing the user that the email entered is used by another user
            flash("There is a user with this email",category="error")
        if len(name) < 2:
            # if the lenght of name is lower than two, we are displaying an error message
            flash("Please enter a valid name",category="error") 
        elif "." and "@" not in list(email) and len(email) < 5:
            # validating email and showing error if it does not valid
            flash("Please enter a valid email",category="error")
        elif password != confirm_password:
            # checking if password matches with confirm_password, and showing an error message if it does not
            flash("Password Mismatch",category="error")
        else:
            # once all the infomation provided by the user is correct, I am filling in the
            # users information into the User table and asigning that to a variable called new_user
            new_user = Admin(name=name,email= email, password= generate_password_hash(password,method="sha256"))
            # adding that user to the database
            db.session.add(new_user)
            # commiting my changes to the database below
            db.session.commit()
            # showing a success message to the user on the frontend 
            flash("Account Created Successfuly",category="success")
            db_user = Admin.query.filter_by(email=email).first()
            # redirecting that user to the admin page
            return redirect(url_for('route.admin', user_id=db_user.id, download=''))
   
    # if the request type is GET i am rendering the sign-up page
    return render_template("html/register.html")

        
@auth.route("/login",methods=["GET","POST"])
def Login():
    # checking the methon type
    if request.method == "POST":
        # collecting the email and password
        email = request.form.get('email')
        password = request.form.get('password')
        # checking the database to see if the email is their
        db_user = Admin.query.filter_by(email=email).first()
        # using an if statement to check if the email is there, and the password for that table match the password 
        # provided.
        if db_user and check_password_hash(db_user.password, password):
            # showing a success message 
            flash(f"Welcome {db_user.name}!", category="success")
            # Taking that user to the admin page
            return redirect(url_for('route.admin', user_id=db_user.id,download=''))
        else:
            # if the informations are not vaild, I am showing an error message
            flash('Email or password incorrect',category="error")
                
    # setting the html template 'template/login.html
    return render_template("html/login.html")

@auth.route("/logout")
def Logout():
    # redirecting to the home page
    return redirect(url_for("route.home"))    