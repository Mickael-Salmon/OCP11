import pytest
from server import app

class TestUpdateClubPoints:
    client = app.test_client()

    def test_update_points(self):
        # Simulate booking places for a club and check if points are updated
        response = self.client.post(
            "/bookPlaces",
            data={
                "places": 3,
                "club": "Club B",
                "competition": "Competition 2"
            }
        )
        assert response.status_code == 200
        # Add assertions to verify club points are updated

if __name__ == "__main__":
    pytest.main()
