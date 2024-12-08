import unittest
from app import app

class TestBooksAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.post('/books', json={"title": "Book 1", "author": "Author 1", "year": 2020})
        self.client.post('/books', json={"title": "Book 2", "author": "Author 2", "year": 2021})

    def test_get_books(self):
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_add_book(self):
        response = self.client.post('/books', json={"title": "Book 3", "author": "Author 3", "year": 2022})
        self.assertEqual(response.status_code, 201)

    def test_update_book(self):
        response = self.client.put('/books/1', json={"title": "Updated Book 1"})
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = self.client.delete('/books/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
