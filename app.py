from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
books = []
members = []

# Books CRUD Operations
@app.route('/books', methods=['POST'])
def add_book():
    """Add a new book to the library."""
    book = request.json
    book['id'] = len(books) + 1
    books.append(book)
    return jsonify({"message": "Book added!", "book": book}), 201

@app.route('/books', methods=['GET'])
def get_books():
    """Retrieve all books with optional pagination."""
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    start = (page - 1) * limit
    end = start + limit
    paginated_books = books[start:end]
    return jsonify({"books": paginated_books, "total": len(books)}), 200

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    """Update an existing book."""
    for book in books:
        if book['id'] == id:
            book.update(request.json)
            return jsonify({"message": "Book updated!", "book": book}), 200
    return jsonify({"message": "Book not found!"}), 404

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    """Delete a book by ID."""
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({"message": "Book deleted!"}), 200

@app.route('/books/search', methods=['GET'])
def search_books():
    """Search books by title or author."""
    query = request.args.get('q', '').lower()
    results = [book for book in books if query in book['title'].lower() or query in book['author'].lower()]
    return jsonify({"results": results}), 200

# Members CRUD Operations
@app.route('/members', methods=['POST'])
def add_member():
    """Add a new member."""
    member = request.json
    member['id'] = len(members) + 1
    members.append(member)
    return jsonify({"message": "Member added!", "member": member}), 201

@app.route('/members', methods=['GET'])
def get_members():
    """Retrieve all members with optional pagination."""
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    start = (page - 1) * limit
    end = start + limit
    paginated_members = members[start:end]
    return jsonify({"members": paginated_members, "total": len(members)}), 200

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    """Update an existing member."""
    for member in members:
        if member['id'] == id:
            member.update(request.json)
            return jsonify({"message": "Member updated!", "member": member}), 200
    return jsonify({"message": "Member not found!"}), 404

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    """Delete a member by ID."""
    global members
    members = [member for member in members if member['id'] != id]
    return jsonify({"message": "Member deleted!"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    
