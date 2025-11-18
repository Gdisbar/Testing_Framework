import pytest 
from src.db import DataBase

@pytest.fixture
def db():
    "Create fresh instance of DataBase"
    database = DataBase()
    yield database # fixture instance
    database.data.clear() # basic dict function (here)

def test_add_user(db):
    db.add_user("1","Ram")
    db.add_user("2","Shyam")
    assert db.get_user("1")=="Ram"

def test_duplicate_add_user(db):
    db.add_user("1","Ram")
    with pytest.raises(ValueError,match="User already exist"):
        db.add_user("1","Jadav")
    
def test_delete_user(db):
    db.add_user("2","Nabin")
    db.delete_user("2")
    assert db.get_user("2")=="User not found"
