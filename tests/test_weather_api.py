import pytest
from src.weather_api import get_weather

def test_get_weather(mocker):
    # Mock requests.get
    mock_get = mocker.patch("src.weather_api.requests.get")
    
    # Set return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

    # Call function
    result = get_weather("Dubai")

    # Assertions
    assert result == {"temperature": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")