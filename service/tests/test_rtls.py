import json


def test_rtls(client):
    """
    GIVEN a valid package name and change_id
    WHEN the rtls API is called
    THEN a response containing the package name is returned
    """
    response = client.get("/rtls/test_pkg/12345")

    assert response.status_code == 200
    data = json.loads(response.data)
    assert "test_pkg" in data['msg']
