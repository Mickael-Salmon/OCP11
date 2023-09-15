import pytest
from server import app, clubs

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestUnknownEmailHandling:

    def test_unknown_email(self, client):
        # Envoi d'un e-mail inconnu
        response = client.post('/showSummary', data={'email': 'unknown@email.com'})
        assert response.status_code == 401  # Le code de statut doit être 401 Unauthorized
        assert b'No account related to this email.' in response.data  # Le message d'erreur doit être présent dans la réponse

    def test_empty_email(self, client):
        # Envoi d'un e-mail vide
        response = client.post('/showSummary', data={'email': ''})
        assert response.status_code == 401  # Le code de statut doit être 401 Unauthorized
        assert b'Please enter your email.' in response.data  # Le message d'erreur doit être présent dans la réponse
