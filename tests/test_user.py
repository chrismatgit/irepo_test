import unittest
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api.Views.routes import app
from api.Models.Users import User
from db import DatabaseConnection
from base_test import BaseTest

class Test_User(BaseTest):
    def setUp(self):
        self.tester = app.test_client(self)
        self.db = DatabaseConnection()

    def test_signup(self):
        account = {
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma12125"
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
            "email": "kelly1212example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": True,
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": 1233,
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": True,
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": 21124,
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": False,
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": 7512345678,
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": 123
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "username": "kellyma1212",
            "password": "password"
        }

        response = self.tester.post(
            'api/v1/login/', content_type ='application/json',
            data=json.dumps(login_info)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn("kellyma1212 successfuly login", reply['message'])
        self.assertEqual(response.status_code, 200)

    def test_login_username_is_empty(self):
        account = {
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "username": "kellyma1212",
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
            "username": "kellyma1212",
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
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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

#     def test_promote_a_user(self):
#         account = {
#             "email": "kelly@example.com",
#             "firstname": "mary",
#             "isAdmin": False,
#             "lastname": "grace",
#             "othernames": "kelly",
#             "password": "1212155454",
#             "phone_number": "07512345678",
#             "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
#             "user_id": 1,
#             "username": "kellym"
#         }

#         response = self.tester.post(
#             '/api/v1/signup/', content_type ='application/json',
#             data=json.dumps(account)
#         )
#         reply = json.loads(response.data.decode())

#         print(response.data)
#         self.assertIn("mary has been created successfuly", reply['message'])
#         self.assertEqual(response.status_code, 201)

#         response = self.tester.patch(
#             '/api/v1/user/promote/1', content_type ='application/json'
#         )
#         print(response.data)
#         self.assertEqual(response.status_code, 200)

    
#     def test_invalid_user_id_to_promote(self):
#         account = {
#             "email": "kelly@example.com",
#             "firstname": "mary",
#             "isAdmin": False,
#             "lastname": "grace",
#             "othernames": "kelly",
#             "password": "1212155454",
#             "phone_number": "07512345678",
#             "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
#             "user_id": 1,
#             "username": "kellym"
#         }

#         response = self.tester.post(
#             '/api/v1/signup/', content_type ='application/json',
#             data=json.dumps(account)
#         )
#         reply = json.loads(response.data.decode())

#         print(response.data)
#         self.assertIn("mary has been created successfuly", reply['message'])
#         self.assertEqual(response.status_code, 201)

#         response = self.tester.patch(
#             '/api/v1/user/promote/2', content_type ='application/json'
#         )
#         print(response.data)
#         self.assertEqual(response.status_code, 404)

    def test_get_all_users(self):
        account = {
            "email": "kelly1212@example.com",
            "firstname": "mary",
            "isadmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "password",
            "phone_number": "07512345678",
            "registered": "24-12-2018",
            "username": "kellyma1212"
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
        response = self.tester.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_auth_welcome(self):
        reply = self.login_user()
        token = reply['token']
        response = self.tester.get(
            '/api/v1/welcome',
            content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'kellyma1212 thanks for using iReporter Api')
        self.assertEqual(response.status_code, 200)


    def tearDown(self):
        self.db.drop_table('users')


