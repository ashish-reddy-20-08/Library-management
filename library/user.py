import logging
from .storage import Storage

# implementation of the basic user class
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        return {"name": self.name, "user_id": self.user_id}

    @staticmethod
    def from_dict(data):
        return User(data['name'], data['user_id'])

# user manager class with the functionalities like add, delete, search ...
class UserManager:
    def __init__(self, storage_file='users.json'):
        self.storage = Storage(storage_file)
        self.users = self.load_users()

    def load_users(self):
        return [User.from_dict(user) for user in self.storage.load()]

    def save_users(self):
        self.storage.save([user.to_dict() for user in self.users])

    def add_user(self, name, user_id):
        if self.search_users(user_id=user_id):
            logging.warning("User with this ID already exists.")
            print("User with this ID already exists.")
            return
        user = User(name, user_id)
        self.users.append(user)
        self.save_users()
        logging.info(f"User added: {name} (User ID: {user_id})")
        print("User added.")

    def update_user(self, user_id, name=None):
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                self.save_users()
                logging.info(f"User updated: {user_id}")
                print("User updated.")
                return
        logging.warning(f"User not found: {user_id}")
        print("User not found.")

    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                self.save_users()
                logging.info(f"User deleted: {user_id}")
                print("User deleted.")
                return
        logging.warning(f"User not found: {user_id}")
        print("User not found.")

    def list_users(self):
        for user in self.users:
            print(user.to_dict())

    def search_users(self, **kwargs):
        results = []
        for user in self.users:
            if all(getattr(user, k) == v for k, v in kwargs.items()):
                results.append(user)
        if not results:
            logging.info("No users found.")
            print("No users found.")
        return results

    def print_search_results(self, results):
        if results:
            for user in results:
                print(user.to_dict())
            logging.info("User is present.")
            print("User is present.")
        else:
            logging.info("User not present.")
            print("User not present.")
