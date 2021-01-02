import os
import unittest
from webapp import app,db
from webapp.model import User

TEST_DB = 'test.db'
class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        basedir =os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        self.assertEqual(app.debug, False)

    def tearDown(self):

        db.session.remove()
        db.drop_all()

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def add_user(self):
        f=User(username="S7bhash",password="passphrase",email="subhash@gmail.com",city="Bangalore",age=18,occupation="student",state="Karnataka")
        db.session.add(f)
        db.session.commit()
        self.assertTrue()



if __name__ == "__main__":
    unittest.main()
