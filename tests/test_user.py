import unittest
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api import app
from api.Models.Users import User

class Test_User(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client()

    def test_signup(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

    
    
    def test_duplicate_username(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("username already taken", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_duplicate_email(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("email already existed", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_invalid_email(self):
        account = {
            "email": "kellyexample.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Email field can not be left empty, is invalid(eg: example@example.com) and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)
  
    def test_empty_email(self):
        account = {
            "email": "",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Email field can not be left empty, is invalid(eg: example@example.com) and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_email_is_not_string(self):
        account = {
            "email": 121231,
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Email field can not be left empty, is invalid(eg: example@example.com) and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_empty_firstname(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Firstname field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)


    def test_firstname_is_not_string(self):
        account = {
            "email": "kelly@example.com",
            "firstname": 12345,
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Firstname field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)


    def test_empty_lastname(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Lastname field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)


    def test_lastname_is_not_string(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": 12234,
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Lastname field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_empty_othername(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("othernames field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)


    def test_orthername_is_not_string(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": 1212121,
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("othernames field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)


    def test_empty_password(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Password field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)


    def test_password_is_not_string(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": 12121,
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Password field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)


    def test_empty_phone_number(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212132",
            "phone_number": "",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("phone_number field can not be left empty and should be a string!", reply['error'])
        self.assertEqual(response.status_code, 400)


    def test_phone_number_is_not_string(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "12121",
            "phone_number": 7512345678,
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("phone_number field can not be left empty and should be a string!", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_empty_username(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212132",
            "phone_number": "781234567",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": ""
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Username field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)


    def test_username_is_not_string(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "12121",
            "phone_number": "7512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": 12265
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Username field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)




    def test_login(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        login_info = {
            "username": "kellym",
            "password": "1212155454"
        }

        response = self.tester.post(
            'api/v1/login/', content_type ='application/json',
            data=json.dumps(login_info)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("kellym successfuly login", reply['message'])
        self.assertEqual(response.status_code, 200)

    def test_login_username_is_empty(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        login_info = {
            "username": "",
            "password": "1212155454"
        }

        response = self.tester.post(
            'api/v1/login/', content_type ='application/json',
            data=json.dumps(login_info)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Username field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_login_username_is_not_string(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        login_info = {
            "username": 121554,
            "password": "1212155454"
        }

        response = self.tester.post(
            'api/v1/login/', content_type ='application/json',
            data=json.dumps(login_info)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Username field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_login_password_is_empty(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        login_info = {
            "username": "kellym",
            "password": ""
        }

        response = self.tester.post(
            'api/v1/login/', content_type ='application/json',
            data=json.dumps(login_info)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Password field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_login_password_is_not_string(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        login_info = {
            "username": "kellym",
            "password": 1221215
        }

        response = self.tester.post(
            'api/v1/login/', content_type ='application/json',
            data=json.dumps(login_info)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Password field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_login_wrong_creditential(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        login_info = {
            "username": "kellym",
            "password": "1221215"
        }

        response = self.tester.post(
            'api/v1/login/', content_type ='application/json',
            data=json.dumps(login_info)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("Wrong username or password", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_promote_a_user(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        response = self.tester.patch(
            '/api/v1/user/promote/1', content_type ='application/json'
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)

    
    def test_invalid_user_id_to_promote(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        response = self.tester.patch(
            '/api/v1/user/promote/2', content_type ='application/json'
        )
        print(response.data)
        self.assertEqual(response.status_code, 404)

    def test_get_all_users(self):
        account = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("mary has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        response = self.tester.get(
            '/api/v1/users/', content_type ='application/json'
        )
        self.assertEqual(response.status_code, 200)


    def test_get_all_users_is_empty(self):
        response = self.tester.get(
            '/api/v1/users/', content_type ='application/json'
        )
        self.assertEqual(response.status_code, 404)

    def test_welcome(self):
        response = self.tester.get('/api/v1/')
        self.assertEqual(response.status_code, 200)


    def tearDown(self):
        User.accounts.clear()


