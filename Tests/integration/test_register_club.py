import pytest
from server import app

class TestRegisterClub:
    client = app.test_client()

    def test_register_new_club(self):
        # Simulate registration of a new club
        response = self.client.post(
            "/registerClub",
            data={
                "name": "New Club",
                "email": "newclub@example.com"
            }
        )
        assert response.status_code == 200
        # Add assertions to verify club registration

if __name__ == "__main__":
    pytest.main()
