async def test_get_via_http_user_mocking_sql_alchemy(client):
    response = client.get("/api/users/1e1054ce-e182-482d-8e09-13febe3d8514")
    response_data = response.json()
    assert len(response_data) > 0
    assert response.status_code == 200
    assert response_data.get("first_name") == "Marcolino"
