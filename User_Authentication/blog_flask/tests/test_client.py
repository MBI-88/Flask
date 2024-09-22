# Test the client

# Packages
import re
import unittest
from app import create_app,db
from app.models import User,Role

# Classes

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)
    
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_home_page(self) -> None:
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTrue('Stranger' in response.get_data(as_text=True))
    
    def test_register_and_login(self) -> None:
        response = self.client.post('/auth/register',data={
            'email':'rootmbi@example.com',
            'username':'Admin',
            'password':'root',
            'password2':'root'
        })
        self.assertEqual(response.status_code,302)
        
        response = self.client.post('/auth/login',data={
            'email':'rootmbi@example.com',
            'password':'root'
        },follow_redirects=True)
        self.assertEqual(response.status_code,200)
        self.assertTrue(re.search('Hello, !',response.get_data(as_text=True)))
        
        self.assertTrue(
            'You have not confirmed your account yet' in response.get_data(as_text=True)
        )
        
        user = User.query.filter_by(email='rootmbi@example.com').first()
        token = user.generate_confirmation_token()
        response = self.client.get('/auth/confirm/{}'.format(token),follow_redirects=True)
        
        user.confirm(token)
        self.assertEqual(response.status_code,200)
        self.assertTrue(
            'You have confirmed your account' in response.get_data(as_text=True)
        )
        
        response = self.client.get('/auth/logout',follow_redirects=True)
        self.assertEqual(response._status_code,200)
        self.assertTrue('You have been logged out' in response.get_data(as_text=True))
        