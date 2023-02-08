from database.db_schema import Admin, Payload


'''
        Using the GIVEN, WHEN, THEN structure, to discribe the test
        
        GIVEN: The initial test model
        WHEN: The senerro that we want to test
        THEN: What is the expected result
'''


def testAdmin():
        '''
        GIVEN a case of Admin model
        WHEN  a new Admin is created
        THEN check if the name, email, and password are defined correctly
        '''
        create_admin = Admin(name = "Tomisin",
        email = "tomisin@gmail.com", password = "tomisin123456")
        assert create_admin.name == 'Tomisin'
        assert create_admin.email == 'tomisin@gmail.com'
        assert create_admin.password == 'tomisin123456'

def testPayload():
        '''
        GIVEN a case of Payload model
        WHEN  the Admin upload data  to the Payload 
        THEN check if the informations are defined correctly
        '''
        create_admin_payload = Payload(
        hotel_name = "Abuda bi",
    review = "This is the best hotel I have ever stayed. I don't feel like going home anymore",
    hotel_country = "Dubai",
    hotel_city = "Abu",
    hotel_address = "Abu Abuda bi",
    expected_impression = "positive",
    bert_impression = 'positive',
                
        )
        assert create_admin_payload.hotel_name == 'Abuda bi'
        assert create_admin_payload.review == "This is the best hotel I have ever stayed. I don't feel like going home anymore" 
        assert create_admin_payload.hotel_country == 'Dubai'
        assert create_admin_payload.hotel_city == 'Abu'
        assert create_admin_payload.hotel_address == 'Abu Abuda bi'
        assert create_admin_payload.expected_impression == 'positive'
        assert create_admin_payload.bert_impression == 'positive'

