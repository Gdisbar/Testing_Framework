import pytest
from unittest.mock import MagicMock
from src.fastapi_sqlalchemy import app, get_db, Product
from fastapi.testclient import TestClient

mock_session = MagicMock()

def override_get_db():
    try:
        yield mock_session
    finally:
        pass

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def mock_db_session():
    return mock_session

client = TestClient(app)

def test_create_product(mock_db_session):
    # Create a mock product that will be returned
    mock_product = Product(id=1, name="Test Product", description="Test Description")
    
    # Configure the mock to simulate db.refresh() setting the id
    def refresh_side_effect(obj):
        obj.id = 1
    
    mock_db_session.refresh.side_effect = refresh_side_effect
    
    response = client.post(
        "/add_products/",  # Fixed: use correct endpoint
        json={"name": "Test Product", "description": "Test Description"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["description"] == "Test Description"
    assert "id" in data

    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once()


def test_get_products(mock_db_session):
    # Mock the query chain
    mock_query = MagicMock()
    mock_db_session.query.return_value = mock_query
    
    # Create mock products
    mock_products = [
        Product(id=1, name="Product 1", description="Description 1"),
        Product(id=2, name="Product 2", description="Description 2")
    ]
    mock_query.all.return_value = mock_products
    
    response = client.get("/get_products/")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Product 1"
    assert data[1]["name"] == "Product 2"
    
    mock_db_session.query.assert_called_once()