from server import app

class TestLoginOut:
    """
    Classe de tests unitaires pour la connexion/déconnexion.

    Cette classe teste la connexion et la déconnexion d'un club.
    """

    client = app.test_client()

    def test_login(self):
        """
        Test de connexion.

        Cette méthode teste le Login
        Le CODE 200 signifie que la connexion s'est bien passée.
        """
        result = self.client.get('/login')
        assert result.status_code == 200

    def test_logout(self):
        """
        Test de déconnexion.

        Cette méthode teste le Logout
        Le CODE 302 signifie que la déconnexion s'est bien passée.
        """
        result = self.client.get('/logout')
        assert result.status_code == 302

