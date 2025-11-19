import pytest
from src.api_service import APIClient,UserService

def test_user_with_mock(mocker):
    mock_api_client = mocker.Mock(APIClient)
    mock_api_client.get_user_data.return_value = {"id":1,"name":"Ramman"}
    service = UserService(mock_api_client) # Instead of calling APIClient we call it's mock version
    result = service.get_username(1)
    assert result=="RAMMAN"
    mock_api_client.get_user_data.assert_called_once_with(1)

