from flask import Flask
import threading
from config import redis_client
from models import Book  # Frontend book model to update the catalogue
import json

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()




def handle_redis_message(message):
    data = json.loads(message['data'])
    event = data.get('event')

    if event == 'book_added':
        # Update Frontend API's database with the new book
        title = data['data']['title']
        author = data['data']['author']
        Book.add_book(title=title, author=author)
        print(f"Book added: {title}")

    elif event == 'book_removed':
        book_id = data['data']['book_id']
        Book.remove_book(book_id)
        print(f"Book removed: {book_id}")

def redis_listener():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('book_events')
    for message in pubsub.listen():
        if message['type'] == 'message':
            handle_redis_message(message)

# Start Redis listener in a separate thread
listener_thread = threading.Thread(target=redis_listener)
listener_thread.start()

