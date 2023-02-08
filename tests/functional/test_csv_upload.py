
import pytest
from app_connector import create_myApp


def test_admin_route_with_wrong_data():
    app = create_myApp()

    with app.test_client() as tc:
        try:
            # When
            post_res = tc.post(
                    '/admin/1', data = dict(
                        file = "static/files/text_DB.pdf",
                        
                    ),follow_redirects= True,
                    )
            # Then 
            assert post_res.status_code == 404
        except:
            assert pytest.raises(ValueError)