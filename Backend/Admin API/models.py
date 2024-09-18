from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.library_admin

users_collection = db.users
books_collection = db.books

class User:
    @staticmethod
    def create_user(firstname, lastname, email):
        user = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "borrowed_books": []
        }
        return users_collection.insert_one(user)

    @staticmethod
    def get_all_users():
        return list(users_collection.find())

class AdminBook:
    @staticmethod
    def add_book(title, author, publisher, category):
        book = {
            "title": title,
            "author": author,
            "publisher": publisher,
            "category": category,
            "is_available": True,
            "borrowed_until": None
        }
        return books_collection.insert_one(book)

    @staticmethod
    def remove_book(book_id):
        return books_collection.delete_one({"_id": book_id})

    @staticmethod
    def get_all_books():
        return list(books_collection.find())

    @staticmethod
    def get_unavailable_books():
        return list(books_collection.find({"is_available": False}))
