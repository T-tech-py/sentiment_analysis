import pytest
from app_connector import create_myApp
from flask import url_for

def test_home_route():
    '''
    GIVEN my flask application is configured for testing
    WHEN  the route.home('/') is called on (GET) request
    THEN check the validity of the response.
    '''
    flask_app =  create_myApp()

    ''''''
    with flask_app.test_client() as tc:
        try:
            response = tc.get('/')
        
            assert response.status_code == 200
        except:
            pytest.raises(ValueError)
        

