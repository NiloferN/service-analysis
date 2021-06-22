from flask import Flask
import json

from service-analysis.app import home

def test_base_route():
    app = Flask(__name__)
    home(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Login'
    assert response.status_code == 200
