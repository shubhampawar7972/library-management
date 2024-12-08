import unittest
from app import app

class TestMembersAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.post('/members', json={"name": "Member 1", "email": "member1@example.com"})
        self.client.post('/members', json={"name": "Member 2", "email": "member2@example.com"})

    def test_get_members(self):
        response = self.client.get('/members')
        self.assertEqual(response.status_code, 200)

    def test_add_member(self):
        response = self.client.post('/members', json={"name": "Member 3", "email": "member3@example.com"})
        self.assertEqual(response.status_code, 201)

    def test_update_member(self):
        response = self.client.put('/members/1', json={"name": "Updated Member 1"})
        self.assertEqual(response.status_code, 200)

    def test_delete_member(self):
        response = self.client.delete('/members/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
