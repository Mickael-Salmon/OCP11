import pytest
import json
from server import app

def load_clubs_from_file():
    with open('clubs.json') as f:
        data = json.load(f)
    return data['clubs']

def load_competitions_from_file():
    with open('competitions.json') as f:
        data = json.load(f)
    return data['competitions']

@pytest.fixture(scope="function")
def initialize_data():
    return {
        'client': app.test_client(),
        'club': load_clubs_from_file(),
        'competition': load_competitions_from_file()
    }

@pytest.fixture
def reset_total_places(initialize_data):
    for club in initialize_data['club']:
        club['total_places'] = 0

# Classe pour tester la réservation de moins de 12 places
class TestLessThan12:
    client = app.test_client()

    @pytest.mark.usefixtures("reset_total_places")
    def test_less_than_12(self):
        with self.client:
            response = self.client.post('/booking_route', data={'places': 11})
            assert response.status_code == 200

# Classe pour tester la réservation avec un club ayant plus de 12 points
class TestMoreThanTwelvePoints:
    client = app.test_client()

    @pytest.mark.usefixtures("reset_total_places")
    def test_more_than_twelve_points(self):
        with self.client:
            response = self.client.post('/booking_route', data={'places': 12})
            assert response.status_code == 200

# Classe pour tester la réservation de plus de 12 places en une seule tentative
class TestMoreThan12OneTry:
    client = app.test_client()

    @pytest.mark.usefixtures("reset_total_places")
    def test_more_than_12_one_try(self):
        with self.client:
            response = self.client.post('/purchasePlaces', data={'places': 13})
            assert response.status_code == 400

# Test pour vérifier la réservation de plus de 12 places en plusieurs tentatives
def test_more_than_twelve_multiple_bookings(initialize_data):
    client = initialize_data['client']
    club = initialize_data['club'][0]
    competition = initialize_data['competition'][0]

    with client:
        response1 = client.post('/booking_route', data={'places': 6})
        assert response1.status_code == 200

        response2 = client.post('/booking_route', data={'places': 7})
        assert response2.status_code == 400
