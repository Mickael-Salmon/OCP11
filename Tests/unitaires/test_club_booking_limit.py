from server import app

# Classe pour tester la réservation de moins de 12 places
class TestLessThan12:
    client = app.test_client()

    def test_less_than_12(self):
        with self.client:
            response = self.client.post('/booking_route', data={'places': 11})
            assert response.status_code == 200
            # Autres assertions ici

# Classe pour tester la réservation avec un club ayant plus de 12 points
class TestMoreThanTwelvePoints:
    client = app.test_client()

    def test_more_than_twelve_points(self):
        with self.client:
            response = self.client.post('/booking_route', data={'places': 12})
            assert response.status_code == 200
            # Autres assertions ici

# Classe pour tester la réservation de plus de 12 places en une seule tentative
class TestMoreThan12OneTry:
    client = app.test_client()

    def test_more_than_12_one_try(self):
        with self.client:
            response = self.client.post('/booking_route', data={'places': 13})
            assert response.status_code == 400
            # Autres assertions ici

# Classe pour tester la réservation de plus de 12 places en plusieurs tentatives
class TestMoreThan12MultipleTry:
    client = app.test_client()

    def test_more_than_12_multiple_try(self):
        with self.client:
            # Première tentative de réservation
            response1 = self.client.post('/booking_route', data={'places': 6})
            assert response1.status_code == 200

            # Deuxième tentative de réservation
            response2 = self.client.post('/booking_route', data={'places': 7})
            assert response2.status_code == 400

            # Autres tentatives de réservation ici
