# Implémenter un test de performance qui utilise locust
from locust import HttpUser, task, between
from tools import load_clubs, load_competitions

class LocustTestServer(HttpUser):
    wait_time = between(1, 5)  # Temps d'attente aléatoire entre 1 et 5 secondes entre les requêtes
    competition = load_competitions()[0]  # Chargement de la première compétition depuis vos données
    club = load_clubs()[0]  # Chargement du premier club depuis vos données

    def on_start(self):
        # Effectue des actions de configuration initiale (peut être utilisé pour se connecter, etc.)
        # Dans cet exemple, nous accédons à la page d'accueil et affichons un résumé du club
        self.client.get("/", name="Home")
        self.client.post("/showSummary", data={'email': self.club["email"]}, name="Show Summary")

    @task
    def reserve_places(self):
        # Simulation de la réservation de places pour une compétition spécifique
        response = self.client.get(
            f"/book/{self.competition['name']}/{self.club['name']}",
            name="Reserve Places"
        )
        # Vous pouvez ajouter des assertions pour vérifier la réponse si nécessaire
        # assert response.status_code == 200

    @task
    def purchase_places(self):
        # Simulation de l'achat de places pour une compétition spécifique
        response = self.client.post(
            "/purchasePlaces",
            data={
                "places": 0,  # Modifier le nombre de places à acheter si nécessaire
                "club": self.club["name"],
                "competition": self.competition["name"]
            },
            name="Purchase Places"
        )
        # Vous pouvez ajouter des assertions pour vérifier la réponse si nécessaire
        # assert response.status_code == 200

    @task
    def view_club_points(self):
        # Simulation de l'affichage des points du club
        self.client.get("/viewClubPoints", name="View Club Points")

