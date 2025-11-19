import sqlite3

class DataBase:
    def __init__(self) -> None:
        self.data = {} # Simulating DB
    
    def add_user(self,user_id:str,name:str):
        if user_id in self.data:
            raise ValueError("User already exist")
        self.data[user_id] = name 

    def get_user(self,user_id:str):
        return self.data.get(user_id,None)
    
    def delete_user(self,user_id:str):
        if user_id in self.data:
            del self.data[user_id]

class SQLiteDataBase:
    def save_user(self,name,age):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name,age) VALUES (?,?)",(name,age))
        conn.commit()
        conn.close()
