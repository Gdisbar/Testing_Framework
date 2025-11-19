import pytest 
from src.db import DataBase,SQLiteDataBase

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
    assert db.get_user("2") is None

@pytest.fixture
def sqlite_db():
    "Create fresh instance of DataBase"
    sqlite_db = SQLiteDataBase()
    yield sqlite_db # fixture instance

def test_save_user(mocker, sqlite_db):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_connection_instance = mock_conn.return_value
    mock_cursor_instance = mock_connection_instance.cursor.return_value

    sqlite_db.save_user("Raman", 23)

    mock_conn.assert_called_once_with("users.db")
    mock_cursor_instance.execute.assert_called_once_with(
        "INSERT INTO users (name,age) VALUES (?,?)", ("Raman", 23)
    )


