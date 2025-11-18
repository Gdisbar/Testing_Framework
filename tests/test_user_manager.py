import pytest 
from src.user_manager import UserManager

@pytest.fixture
def user_manager():
    "Create fresh new instance"
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("Ram123","ram123@gmail.com")==True
    assert user_manager.get_user("Ram123")=="ram123@gmail.com"
    assert user_manager.get_user("Bhola123")=="User not found"


def test_duplicate_add_user(user_manager):
    user_manager.add_user("Ram123","ram123@gmail.com")
    with pytest.raises(ValueError):
        user_manager.add_user("Ram123","ram123@another_mail.com")


"""This will not create a new instance"""
# user_manager = UserManager()

# def test_add_user():
#     assert user_manager.add_user("Ram123","ram123@gmail.com")==True
#     assert user_manager.get_user("Ram123")=="ram123@gmail.com"
#     assert user_manager.get_user("Bhola123")=="User not found"


# def test_duplicate_add_user():
#     user_manager.add_user("Ram123","ram123@gmail.com")
#     with pytest.raises(ValueError):
#         user_manager.add_user("Ram123","ram123@another_mail.com")
