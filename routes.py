
# importing flask framework
from flask import Flask, flash, render_template, request, redirect, url_for
# importing the os module
import os
from os.path import pathsep
from flask import Blueprint,send_from_directory, send_file
from csv_logic.csvLogic import CsvLogic
from database.db_schema import Payload, Admin


route =  Blueprint("route",__name__) 
HOTEL_PIC = ['../static/img/team/hotel8.jpg','../static/img/team/hotel2.jpg',
    '../static/img/team/hotel3.jpg', '../static/img/team/hotel9.jpg', '../static/img/team/hotel4.jpg', 
    '../static/img/team/hotel1.jpg', '../static/img/team/hotel6.jpg'
    ]

@route.route("/",methods=["GET","POST"])
def home():
    db_data = Payload.query.limit(6).all()
    all_hotels = Payload.query.all()
  
    if request.method == "POST":
        name = request.form.get("name").title()
        print(name)
        hotel_detail = Payload.query.filter_by(hotel_name=name).all()
        if len(hotel_detail) > 0:
            return render_template("html/preview_multiple.html",details = hotel_detail)
        #    return redirect(url_for("route.preview", details =hotel_detail))
        else:
            flash(f"There is no record for {name} ",category="error")
    # setting the html template 'template/index.html
    return render_template("index.html", hotels = db_data , all_hotels = all_hotels, hotel_pic = HOTEL_PIC)

@route.route("/admin/<user_id>",methods =["GET,POST"])
def admin(user_id):

            # setting the html template 'template/admin.html
            return render_template("html/admin.html", user_id = user_id, download='<download>')
       


@route.route("/preview/<name>")
def preview(name):
    hotel_detail = Payload.query.filter_by(hotel_name=name).all()
    # setting the html template 'template/setup.html
    return render_template("html/preview.html",details = hotel_detail)

@route.route("/hotels")
def hotels():
    all_hotels = Payload.query.all()
    # setting the html template 'template/all_hotels.html
    return render_template("html/all_hotels.html",hotels = reversed(all_hotels),hotel_pic = HOTEL_PIC)


@route.route("/download/<download>",methods=['GET', 'POST'])
def download(download):
    from app_connector import create_myApp
    app= create_myApp()
    uploads = os.path.join(app.root_path,app.config['UPLOAD_FOLDER'],)
    # setting the html template 'template/loading_animation.html
    return send_from_directory(directory=uploads, path=download, as_attachment=True)

