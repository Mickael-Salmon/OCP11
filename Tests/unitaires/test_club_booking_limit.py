import pytest
from server import app

@pytest.fixture
def clubs_list():
    return [
        {"name": "Club 1", "total_places": 0},
        {"name": "Club 2", "total_places": 0},
        # Ajoutez plus de clubs ici selon vos besoins
    ]

@pytest.fixture
def reset_total_places(clubs_list):
    for club in clubs_list:
        club['total_places'] = 0

# Classe pour tester la réservation de moins de 12 places
class TestLessThan12:
    client = app.test_client()

    @pytest.mark.usefixtures("reset_total_places")
    def test_less_than_12(self):
        with self.client:
            response = self.client.post('/booking_route', data={'places': 11})
            assert response.status_code == 200
            # Autres assertions ici

# Classe pour tester la réservation avec un club ayant plus de 12 points
class TestMoreThanTwelvePoints:
    client = app.test_client()

    @pytest.mark.usefixtures("reset_total_places")
    def test_more_than_twelve_points(self):
        with self.client:
            response = self.client.post('/booking_route', data={'places': 12})
            assert response.status_code == 200
            # Autres assertions ici

# Classe pour tester la réservation de plus de 12 places en une seule tentative
class TestMoreThan12OneTry:
    client = app.test_client()

    @pytest.mark.usefixtures("reset_total_places")
    def test_more_than_12_one_try(self):
        with self.client:
            response = self.client.post('/purchasePlaces', data={'places': 13})
            assert response.status_code == 400
            # Autres assertions ici

# Classe pour tester la réservation de plus de 12 places en plusieurs tentatives (méthode 1)
class TestMoreThan12MultipleTry:
    client = app.test_client()

    @pytest.mark.usefixtures("reset_total_places")
    def test_more_than_12_multiple_try(self):
        with self.client:
            # Première tentative de réservation
            response1 = self.client.post('/booking_route', data={'places': 6})
            assert response1.status_code == 200

            # Deuxième tentative de réservation
            response2 = self.client.post('/booking_route', data={'places': 7})
            assert response2.status_code == 400

# Classe pour tester la réservation de plus de 12 places en plusieurs tentatives (méthode 2)
class TestClubBookingLimit:
    client = app.test_client()

    def setUp(self):
        self.client = app.test_client()
        self.club = [{"name": "Club 1"}]
        self.competition = [{"name": "Competition 1"}]

    @pytest.mark.usefixtures("reset_total_places")
    def test_more_than_twelve_multiple_bookings(self):
        # Première réservation de 6 places, devrait réussir
        result1 = self.client.post(
            "/purchasePlaces",
            data={
                "places": 6,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )
        assert result1.status_code == 200
        assert "Great-booking complete!" in result1.data.decode()

        # Deuxième réservation de 7 places, devrait échouer car le total serait 13
        result2 = self.client.post(
            "/purchasePlaces",
            data={
                "places": 7,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )
        assert result2.status_code == 400
        assert "more than 12 places in a competition." in result2.data.decode()
