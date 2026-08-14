from gimnasio_app.views.web_view import create_app


def test_week_page_returns_ok():
    client = create_app().test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_week_page_shows_all_days_and_monday_exercise():
    client = create_app().test_client()

    body = client.get("/").get_data(as_text=True)

    for day in ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes"):
        assert day in body
    assert "Sentadilla o prensa de piernas" in body
