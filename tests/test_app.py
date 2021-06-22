import pytest

def login(client, username, password):
    return client.post('/', data=dict(
        username="saran@gmail.com",
        password="saran123"
    ), follow_redirects=True)

