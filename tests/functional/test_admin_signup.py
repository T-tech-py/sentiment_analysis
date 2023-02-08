
import json
import pytest
from app_connector import create_myApp
from flask import url_for
from werkzeug.security import generate_password_hash,check_password_hash



def test_signup_route():
    '''
    GIVEN my flask application is configured for testing
    WHEN  the ('/setup') is called on (GET) request
    THEN check if it returns a statuscode of 200.
    '''
    app = create_myApp()
    #  Given 
    with app.test_client() as tc:
        # When
        response = tc.get('/setup')
        # Then
        assert response.status_code == 200
    
       
        

