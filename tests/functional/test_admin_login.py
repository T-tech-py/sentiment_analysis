
import json
import pytest
from app_connector import create_myApp
from flask import url_for
from werkzeug.security import generate_password_hash,check_password_hash



def test_login_route():
    '''
    GIVEN my flask application is configured for testing
    WHEN  the ('/login') is called on (GET) request
    THEN check the validity of the response.
    '''
    app = create_myApp()
    #  Given 
    with app.test_client() as tc:
        # When
        response = tc.get('/login')
        # Then
        assert response.status_code == 200
    
       
        

def test_login_route_with_data(database_with_admin):

    # When
    post_res = database_with_admin.post(
            '/login', data = dict(
                email = "tomisin2@gmail.com",
                password = generate_password_hash("jerry12345")
            ),follow_redirects= True,
            )
    # Then 
    assert post_res.status_code == 200

# login with
def test_login_route_with_wrong_data(database_with_admin):
    try:
        # When
        post_res = database_with_admin.post(
                '/login', data = dict(
                    email = "frank@gmail.com",
                    password = generate_password_hash("12345jerry")
                ),follow_redirects= True,
                )
        # Then 
    except:
        assert pytest.raises(ValueError)