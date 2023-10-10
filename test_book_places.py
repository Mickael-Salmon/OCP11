import pytest

from server import app

class TestBookPlaces:
    client = app.test_client()

    def test_book_places(self):
        # Simulate booking places for a club
        response = self.client.post(
            "/bookPlaces",
            data={
                "places": 5,
                "club": "Club A",
                "competition": "Competition 1"
            }
        )
        assert response.status_code == 200


if __name__ == "__main__":
    pytest.main()
