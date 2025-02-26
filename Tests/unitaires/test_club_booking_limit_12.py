﻿import server
from server import app

class TestMoreThanTwelvePoints:
    client = app.test_client()
    competition = [
        {
            "name": "Test",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "40"
        }
    ]

    club = [
        {
            "name": "Test club",
            "email": "test_club@email.com",
            "points": "60"
        }
    ]

    places_booked = [
        {
            "competition": "Test",
            "booked": [5, "Test club"]
        }
    ]

    def setup_method(self):
        server.competitions = self.competition
        server.clubs = self.club
        server.places_booked = self.places_booked

    def test_less_than_twelve(self):
        booked = 5

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": booked,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )

        assert result.status_code == 200  # HTTP 200 OK means the request was successful

    def test_more_than_twelve_once(self):
        booked = 13

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": booked,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )

        assert result.status_code == 400  # HTTP 400 Bad Request means the request was invalid

    def test_more_than_twelve_added(self):
        server.clubs[0]['total_places']['Test'] = 5  # Already 5 places booked
        booked = 8

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": booked,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )

        assert result.status_code == 400  # HTTP 400 Bad Request means the request was invalid
