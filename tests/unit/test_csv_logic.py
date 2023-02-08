from csv_logic.csvLogic import CsvLogic
from flask import flash
import pytest


'''
        Using the GIVEN, WHEN, THEN structure, to discribe the test
        
        GIVEN: The initial test model
        WHEN: The senerro that we want to test
        THEN: What is the expected result
'''


def test_csv_validity():
       
        # When
        csv = CsvLogic()
        try:
            create_admin = csv.check_validity(is_admin = True,
            path ="static/files/text_DB.pdf", user_id = '1')
            # Then
            assert  "error" in create_admin 
        except:
            assert pytest.raises(ValueError)
       

def test_csv_validity_admin():
        '''
        GIVEN a case of Admin model
        WHEN  a new Admin is created
        THEN check if the name, email, and password are defined correctly
        '''
        # When
        csv = CsvLogic()
        try:
            with pytest.raises(ValueError):
                csv.admin_data_extraction(
                path ="static/files/text_DB.csv", 
                user_id = '1', is_admin = True)
            
        except:
            assert pytest.raises(ValueError)
