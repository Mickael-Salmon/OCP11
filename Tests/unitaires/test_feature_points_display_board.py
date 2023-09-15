import pytest
from server import app, clubs

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestPointsDisplayBoard:

    def test_display_board(self, client):
        # Accéder à la page du tableau d'affichage des points
        response = client.get('/viewClubPoints')
        assert response.status_code == 200  # Vérifier que la page se charge correctement

        # Vérifier si les points des clubs sont affichés
        for club in clubs:
            assert bytes(club['name'], 'utf-8') in response.data  # Vérifier que le nom du club est présent
            assert bytes(str(club['points']), 'utf-8') in response.data  # Vérifier que les points du club sont présents
