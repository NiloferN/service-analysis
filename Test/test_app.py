from app import index
def test_base_route():
    app = Flask(__name__)
    home(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Login'
    assert response.status_code == 200
    
#from app import index


#def test_index():
 #   assert index() == "Hello, world!"
