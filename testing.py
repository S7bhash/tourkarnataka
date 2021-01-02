import os
import unittest
from webapp import app, db


class FlaskTestcase(unittest.TestCase):

    def test_login(self):
        tester=app.test_client(self)
        response=tester.get('/login',content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_signup(self):
        tester=app.test_client(self)
        response=tester.get('/signup',content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_home(self):
        tester=app.test_client(self)
        response=tester.get('/',content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_info(self):
        tester=app.test_client(self)
        response=tester.get('/bangalore',content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_admin(self):
        tester=app.test_client(self)
        response=tester.get('/admin',content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_reco(self):
        tester=app.test_client(self)
        response=tester.get('/recommendations',content_type='html/text')
        self.assertEqual(response.status_code,200)



if __name__ == "__main__":
    unittest.main()
