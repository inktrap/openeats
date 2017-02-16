from django_webtest import WebTest
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class accountViewsTestCase(WebTest):
    fixtures = ['test_user_data.json']
    setup_auth = False
    def test_login(self):
        """used to test the login form"""

        #sanity check to make sure the data loaded
        user = User.objects.get(username="testuser")
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('password'))

        #login to the form
        form = self.app.get(reverse('auth_login')).forms[1]
        form['username'] = 'testuser'
        form['password'] = 'password'
        resp = form.submit()
        self.assertEqual(resp.status, '302 Found')
        self.assertEqual(resp.location, 'http://localhost:80' + reverse('recipe_index'))

    def test_bad_login(self):
        """make sure an error is thrown when someone can't login"""
        form = self.app.get(reverse('auth_login')).forms[1]
        form['username'] = 'testuser'
        form['password'] = 'badpassword'
        resp = form.submit()
        self.assertEqual(resp.status, '200 Ok')

    def test_create_user(self):
        """test that a user can be created"""
        form = self.app.get(reverse('registration_register')).forms[1]
        form['username'] = 'newuser'
        form['email'] = 'newUser@yahoo.com'
        form['password1'] = 'password'
        form['password2'] = 'password'
        resp = form.submit().follow()
        self.assertTrue('Thank you' in resp.body)

        #check the signal on save of a new user created a profile for the user
        profile = self.app.get(reverse('profiles_profile_detail', kwargs={'username':'newuser'}))
        self.assertTrue(profile.status, '200 OK')

        #check a unknown user throws a 404 on the profile page
        profile = self.app.get(reverse('profiles_profile_detail', kwargs={'username':'baduser'}),status=404)
        self.assertTrue(profile.status, '404 Not Found')

        

