import server
from server import app

class TestBookPastCompetition:
    """
    Classe de test pour tester la réservation de places pour des compétitions passées.

    Cette classe de test utilise pytest pour tester la réservation de places pour des compétitions passées.
    """

    client = app.test_client()
    competitions = [
        {
            "name": "Test Closed",
            "date": "2020-01-01 00:00:00",
            "places": 10,
            "closed": True
        },
        {
            "name": "Test Open",
            "date": "2024-01-01 00:00:00",
            "places": 10,
            "closed": False
        }
    ]

    club = [
        {
            "name": "Test Club",
            "email": "club_email@test.com",
            "points": 20,
        }
    ]

    def setup_method(self):
        """
        Méthode de setup pour les tests.

        Cette méthode est lancée avant chaque test.
        Elle permet de créer un contexte pour les tests.
        """
        server.competitions = self.competitions
        server.clubs = self.club

    def test_booking_when_competition_is_closed(self):
        """
        Test de réservation de places pour une compétition terminée.

        Cette méthode renvoie une requête GET pour réserver des places pour une compétition passée.
        CODE 400 : La compétition est terminée.
        """
        with self.client:
            response = self.client.get("/book/Test Closed/Test Club")
            assert response.status_code == 400

    def test_booking_when_competition_is_open(self):
        """
        Test de réservation de places pour une compétition ouverte.

        Cette méthode renvoie une requête GET pour réserver des places pour une compétition ouverte.
        CODE 200 : Places réservées.
        """
        with self.client:
            response = self.client.get("/book/Test Open/Test Club")
            assert response.status_code == 200

    def test_booking_when_competition_doesnt_exist(self):
        """
        Test de réservation de places pour une compétition qui n'existe pas.

        Cette méthode renvoie une requête GET pour réserver des places pour une compétition qui n'existe pas.
        CODE 404 : La compétition n'existe pas.
        """
        with self.client:
            response = self.client.get("/book/Non Existent/Test Club")
            assert response.status_code == 404
