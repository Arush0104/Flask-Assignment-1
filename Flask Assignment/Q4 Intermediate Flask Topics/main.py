from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

books = [
    {"id": 1, "title": "Hands-On Machine Learning", "author": "Aurelien Geron"},
    {"id": 2, "title": "Introduction to Algorithms", "author": "Thomas Cormen"},
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    updated_data = request.get_json()
    book.update(updated_data)
    return jsonify(book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book["id"] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
