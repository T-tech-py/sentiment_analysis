from ast import Delete
from os import remove
from tkinter import Y
import pytest
from app_connector import create_myApp,db
from database.db_schema import Admin, Payload
from werkzeug.security import generate_password_hash,check_password_hash

@pytest.fixture(scope="session")
def flask_app():
    app = create_myApp()
    client = app.test_client()
    context = app.test_request_context()
    context.push()

    yield client
    context.pop()


@pytest.fixture(scope="session")
def empty_database(flask_app):
    db.create_all()
    yield flask_app
    db.session.commit()
    db.drop_all()

@pytest.fixture
def database_with_admin(empty_database):
    admin = Admin(name="tomisin", email="tomisin2@gmail.com",password=generate_password_hash("jerry12345"))
    db.session.add(admin)
    # payload = Payload(hotel_name= "Abuda bi",hotel_city="Abu", hotel_country="Dubai",hotel_address="2 abu street",review="I love this please",expectations="positive", bert_impression="positive")
    # db.session.add(payload)
    db.session.commit()
    yield empty_database
    db.session.delete(admin)
    # db.session.execute(Delete(Payload))
    db.session.commit()

