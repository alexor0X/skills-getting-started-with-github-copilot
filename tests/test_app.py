from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    original_participants = list(activities["Chess Club"]["participants"])

    try:
        response = client.delete(
            "/activities/Chess%20Club/participants/michael%40mergington.edu"
        )

        assert response.status_code == 200
        assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
        assert response.json()["message"].startswith("Unregistered")
    finally:
        activities["Chess Club"]["participants"] = original_participants
