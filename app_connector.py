import os
from flask import Flask, flash, redirect, render_template, request, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



db = SQLAlchemy()
DB_NAME = "My_database.db"

def create_myApp():
    app = Flask(__name__,template_folder= "templates",)
    # enablling bugging mode
    app.config["DEBUG"] = True
    # enabling our secret-key 
    app.config['SECRET_KEY'] = "Teeto_sentiment-analysis-pipline"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    # Uploading folder directory 
    UPLOAD_FOLDER = "static/files"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Importing  blueprint
    from authentications.authenticate import auth
    from routes import route
    from database.db_schema import Admin
    # importing csv
    from csv_logic.csvLogic import CsvLogic
    # initializer 
    my_csv_logic = CsvLogic()
    
    # registering our blueprints route's for authentication
    app.register_blueprint(auth, url_prefix = "/")
    app.register_blueprint(route, url_prefix = "/")

    def create_database(application):
        if not os.path.exists("db/db_schema"+ DB_NAME):
            db.create_all(app=application)

    create_database(app)

    @app.route('/admin/<user_id>', methods=['GET','POST'])
    def uploadedFile(user_id):
        if request.method == "GET":
            check_userId = Admin.query.filter_by(id=user_id).first()
            if check_userId:
                return render_template("html/admin.html")
            else:
                flash("Unauthorize", category="error")
                return render_template("html/error.html")
        # checking the request type
        if request.method == "POST":
            #getting the uploaded file
            uploaded_file = request.files['file']
            # checking if a file is picked before the submit button is pressed
            if uploaded_file.filename == '':
                # telling the user to upload a file before pressing the submit button
                flash("Please upload a file.", category="error")
                download_link= ''
                return render_template("html/admin.html", user_id= user_id, path= download_link,) 
            elif uploaded_file.filename != '':
                # setting file path
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
                # save the file
                uploaded_file.save(file_path)
                # calling the needed csv logic.
                download_link = my_csv_logic.check_validity(file_path,is_admin= True, user_id=user_id)
                
                
            return render_template("html/admin.html", user_id= user_id, path= download_link,) 
    
    return app
