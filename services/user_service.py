import pandas as pd
from repositories.user_repository import UserRepository

class UserService:
    repository = UserRepository()

    @staticmethod
    def create_user(name, age):
        return UserService.repository.create_user(name, age)

    @staticmethod
    def get_all_users():
        return UserService.repository.get_all_users()

    @staticmethod
    def delete_user(name):
        return UserService.repository.delete_user(name)
    
    @staticmethod
    def upload_users(file_data):
        df = pd.read_csv(file_data)
        for _, row in df.iterrows():
            UserService.create_user(row["Name"], row['Age'])

    @staticmethod
    def average_age():
        users = UserService.get_all_users()
        df = pd.DataFrame(list(users.items()), columns=["name", "age"])
        df["first_char"] = df["name"].str[0]
        avg_age_by_group = df.groupby("first_char")["age"].mean().to_dict()
        return avg_age_by_group