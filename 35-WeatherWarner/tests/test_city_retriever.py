from weather_warner.city_retriever import CityRetriever


def test_get_city_coordinates_success(monkeypatch):
    # fake API response: list with one item containing lat/lon
    fake_response = [{"lat": 51.5074, "lon": -0.1278}]

    called = {"count": 0}

    def fake_get_request(url, params=None):
        print(f"Fake get_request called with url: {url}, params: {params}")
        called["count"] += 1
        return fake_response

    # patch the get_request name used inside city_retriever module
    monkeypatch.setattr("weather_warner.city_retriever.get_request", fake_get_request)

    retriever = CityRetriever(api_key="dummy")

    coords = retriever.get_city_coordinates("London", api_key="dummy")

    assert coords == {"lat": 51.5074, "lon": -0.1278}

    # cached: calling again should return same coords and not call the request again
    coords2 = retriever.get_city_coordinates("London", api_key="dummy")

    assert coords2 is coords
    assert called["count"] == 1


def test_get_city_coordinates_failure(monkeypatch):
    # simulate failed request (None or empty) -> should return empty dict
    monkeypatch.setattr("weather_warner.city_retriever.get_request", lambda url, params=None: None)

    retriever = CityRetriever(api_key="dummy")
    coords = retriever.get_city_coordinates("Nowhere", api_key="dummy")

    assert coords == {}
