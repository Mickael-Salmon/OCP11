import pytest
from server import app, clubs, competitions

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestPointUpdatesNotReflected:

    def setup_method(self):
        # Initialisation des données pour les tests
        for club in clubs:
            club['points'] = 100  # Mettre tous les clubs à 100 points

    def test_point_updates(self, client):
        # Effectuer une réservation qui coûte 30 points (10 places * 3 points/place)
        response1 = client.post('/purchasePlaces', data={'places': 10, 'competition': 'Spring Festival', 'club': 'Simply Lift'})
        assert response1.status_code == 200  # ou le code de statut attendu

        # Vérifier si les points du club ont été déduits correctement
        club = [c for c in clubs if c['name'] == 'Simply Lift'][0]
        assert club['points'] == 70  # 100 - 30 = 70
