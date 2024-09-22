# Test with selenium

# Packages
import re,threading,time,unittest
from selenium import webdriver
from app import create_app,db
from app.models import Role,User,Post

# Classes
class SeleniumTestCase(unittest.TestCase):
    client = None
    
    @classmethod
    def setUpClass(cls) -> None:
        options = webdriver.FirefoxOptions()
        options.add_argument('headless')
        
        try:
            cls.client = webdriver.Firefox(options=options)
        except:
            pass
        
        if cls.client:
            cls.app = create_app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()
        
            import logging
            logger = logging.getLogger('wekzeug')
            logger.setLevel('ERROR')
            
            db.create_all()
            Role.insert_roles()
            User.fake_users(10)
            Post.fake_posts(10)
            
            admin_role = Role.query.filter_by(name='Administrator').first()
            admin = User(email='john@example.com',username='john',password='cat',
                         role=admin_role,confirmed=True)
            db.session.add(admin)
            db.session.commit()
            
            cls.server_thread = threading.Thread(target=cls.app.run,kwargs={'debug':False})
            cls.server_thread.start()
            time.sleep(1)
    
    @classmethod
    def tearDownClass(cls):
        if cls.client:
            # stop the flask server and the browser
            cls.client.get('http://localhost:5000/shutdown')
            cls.client.quit()
            cls.server_thread.join()

            # destroy database
            db.drop_all()
            db.session.remove()

            # remove application context
            cls.app_context.pop()

    def setUp(self):
        if not self.client:
            self.skipTest('Web browser not available')

    def tearDown(self):
        pass
    
    def test_admin_home_page(self):
        # navigate to home page
        self.client.get('http://localhost:5000/')
        self.assertTrue(re.search('Hello,\s+Stranger!',
                                  self.client.page_source))

        # navigate to login page
        self.client.find_element_by_link_text('Log In').click()
        self.assertIn('<h1>Login</h1>', self.client.page_source)

        # login
        self.client.find_element_by_name('email').\
            send_keys('john@example.com')
        self.client.find_element_by_name('password').send_keys('cat')
        self.client.find_element_by_name('submit').click()
        self.assertTrue(re.search('Hello,\s+john!', self.client.page_source))

        # navigate to the user's profile page
        self.client.find_element_by_link_text('Profile').click()
        self.assertIn('<h1>john</h1>', self.client.page_source)
            