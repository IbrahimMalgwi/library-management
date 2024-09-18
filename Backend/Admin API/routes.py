from flask import Flask, request, jsonify
from models import User, AdminBook
from schemas import AdminUserSchema, AdminBookSchema
from bson.objectid import ObjectId

app = Flask(__name__)

user_schema = AdminUserSchema()
users_schema = AdminUserSchema(many=True)
book_schema = AdminBookSchema()
books_schema = AdminBookSchema(many=True)

# Endpoint to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    AdminBook.add_book(
        title=data['title'],
        author=data['author'],
        publisher=data.get('publisher'),
        category=data.get('category')
    )
    return jsonify({"message": "Book added successfully!"}), 201

# Endpoint to remove a book by ID
@app.route('/books/<book_id>', methods=['DELETE'])
def remove_book(book_id):
    AdminBook.remove_book(ObjectId(book_id))
    return jsonify({"message": "Book removed successfully!"}), 200

# Endpoint to list all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.get_all_users()
    return users_schema.jsonify(users), 200

# Endpoint to list unavailable books
@app.route('/books/unavailable', methods=['GET'])
def get_unavailable_books():
    books = AdminBook.get_unavailable_books()
    return books_schema.jsonify(books), 200

if __name__ == '__main__':
    app.run(debug=True)
