
class DataBase:
    def __init__(self) -> None:
        self.data = {} # Simulating DB
    
    def add_user(self,user_id:str,name:str)->None:
        if user_id in self.data:
            raise ValueError("User already exist")
        self.data[user_id] = name 

    def get_user(self,user_id:str):
        return self.data.get(user_id,None)
    
    def delete_user(self,user_id:str):
        if user_id in self.data:
            del self.data[user_id]


class UserManager:
    def __init__(self) -> None:
        self.users = {}
    
    def add_user(self,username:str,email:str)->bool:
        if username in self.users:
            raise ValueError("User already exist")
        self.users[username] = email
        return True
    
    def get_user(self,username:str)->str:
        return self.users.get(username,"User not found")