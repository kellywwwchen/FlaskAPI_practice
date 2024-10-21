import unittest
from flask import Flask
from views.user_view import bp as user_bp
class TestCreateUserAPI(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.register_blueprint(user_bp)
        self.client = app.test_client()
        self.client.testing = True

    # TC1: User name is empty when request to create user API
    def test_create_user_empty_name(self):
        response = self.client.post('/users/create_user', json={'age': 25})
        self.assertEqual(response.status_code, 400)
        self.assertIn('name or age cannot be empty', response.get_json()['error'])

    # TC2: User age is 999 when request to create user API
    def test_create_user_invalid_age(self):
        response = self.client.post('/users/create_user', json={'name': 'John Doe', 'age': 999})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Age must be more than 0 or less than 150', response.get_json()['error'])

if __name__ == '__main__':
    unittest.main()
