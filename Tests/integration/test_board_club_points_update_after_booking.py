import server
from server import app

class TestClubPointsUpdateAfterBooking:
    """
    Classe de tests pour vérifier la mise à jour des points d'un club après une réservation.
    """
    client = app.test_client()

    # Données de test pour les compétitions et les clubs
    test_competition_data = [
        {
            "name": "TestCompetition",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        }
    ]

    test_club_data = [
        {
            "name": "TestClub",
            "email": "test_club@email.com",
            "points": "10"
        }
    ]

    def setup_method(self):
        """
        Méthode de configuration exécutée avant chaque test.
        """
        # Initialisation des données du serveur
        server.competitions = self.test_competition_data
        server.clubs = self.test_club_data

    def test_points_update_after_booking(self):
        """
        Teste si les points d'un club sont correctement mis à jour après une réservation.
        """
        # Récupérer les points initiaux du club pour le test
        initial_club_points = int(self.test_club_data[0]["points"])

        # Nombre de places à réserver
        num_places_to_book = 1

        # Effectuer une réservation
        self.client.post(
            "/purchasePlaces",
            data={
                "places": num_places_to_book,
                "club": self.test_club_data[0]["name"],
                "competition": self.test_competition_data[0]["name"]
            }
        )

        # Récupérer la page affichant les points des clubs
        response = self.client.get("/viewClubPoints")

        # Vérifier le statut HTTP de la réponse
        assert response.status_code == 200

        # Calculer les points attendus du club après la réservation
        expected_club_points = initial_club_points - (num_places_to_book * 3)

        # Vérifier si les points du club sont correctement affichés sur la page
        assert f"<td>{self.test_club_data[0]['name']}</td>" in response.data.decode()
        assert f"<td>{expected_club_points}</td>" in response.data.decode()
