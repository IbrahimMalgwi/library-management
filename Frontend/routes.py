from flask import Flask, request, jsonify
from models import db, User, Book
from schemas import UserSchema, BookSchema
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

user_schema = UserSchema()
book_schema = BookSchema()
books_schema = BookSchema(many=True)

# Endpoint to enroll a user
@app.route('/users', methods=['POST'])
def enroll_user():
    data = request.json
    new_user = User(
        firstname=data['firstname'],
        lastname=data['lastname'],
        email=data['email']
    )
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), 201

# Endpoint to list all available books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.filter_by(is_available=True).all()
    return books_schema.jsonify(books), 200

# Endpoint to borrow a book by ID
@app.route('/borrow/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    book = Book.query.get(book_id)
    if not book or not book.is_available:
        return jsonify({"message": "Book not available"}), 404

    data = request.json
    days = data.get('days', 7)
    book.is_available = False
    book.borrowed_until = datetime.now() + timedelta(days=days)
    db.session.commit()

    return book_schema.jsonify(book), 200

if __name__ == '__main__':
    app.run(debug=True)
