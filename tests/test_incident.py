import unittest
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api.Views.routes import app
from api.Models.Incidents import Incident
from db import DatabaseConnection
from base_test import BaseTest

class Test_Incident(BaseTest):
    def setUp(self):
        self.tester = app.test_client(self)
        self.db = DatabaseConnection()

    def test_create_incident(self):
        reply = self.login_user()
        token = reply['token']

        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

    def test_create_comment_is_empty(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("comment field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_create_comment_is_not_a_string(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": True,
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("comment field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)
    
    def test_create_createdBy_is_not_an_integer(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": "1",
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("createdby field can not be left empty and should be an integer", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_create_createdBy_is_empty(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "True",
            "createdby": "",
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("createdby field can not be left empty and should be an integer", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_create_location_is_not_a_string(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": 101010,
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("location field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_create_location_is_empty(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("location field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_image_has_an_invalid_format(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.xls",
            "inctype": "red-flag",
            "location": "12121",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("image has an invalid format(eg: image.png  or image.jpg", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_image_has_an_empty_name(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": ".jpg",
            "inctype": "red-flag",
            "location": "11010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("image has an invalid format(eg: image.png  or image.jpg", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_image_has_a_invalid_input(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": True,
            "inctype": "red-flag",
            "location": "11010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("Something went wrong with your inputs", reply['error'])
        self.assertEqual(response.status_code, 400)


    def test_video_has_invalid_format(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "inctype": "red-flag",
            "location": "11010",
            "status": "draft",
            "video": "video.xls"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("video has an invalid format(eg: video.mp4  or video.avi)", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_video_has_an_invalid_name(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "inctype": "red-flag",
            "location": "11010",
            "status": "draft",
            "video": ".avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("video has an invalid format(eg: video.mp4  or video.avi)", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_video_has_invalid_input(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "inctype": "red-flag",
            "location": "11010",
            "status": "draft",
            "video": True
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("Something went wrong with your inputs", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_incType_is_empty(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "inctype": "",
            "location": "11010",
            "status": "draft",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("inctype field can not be left empty, it should be eg: red-flag or intervention and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_incType_is_not_a_string(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "inctype": 1215,
            "location": "11010",
            "status": "draft",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("inctype field can not be left empty, it should be eg: red-flag or intervention and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    
    def test_incType_is_not_red_flag_or_intervention(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "some comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "inctype": "crime",
            "location": "11010",
            "status": "draft",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("inctype field can not be left empty, it should be eg: red-flag or intervention and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_incType_is_intervention(self):
        reply = self.login_user()
        token = reply['token']

        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "intervention",
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("intervention has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

    def test_incType_is_red_flag(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)


    def test_status_is_not_a_string(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": False,
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("status field can not be left empty, it should be eg: draft, resolved, under_investigation or rejected                 and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_status_is_empty(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("status field can not be left empty, it should be eg: draft, resolved, under_investigation or rejected                 and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    
    def test_status_is_string_but_invalid(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "late",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("status field can not be left empty, it should be eg: draft, resolved, under_investigation or rejected                 and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_status_is_draft(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)


    def test_status_is_under_investigation(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "under_investigation",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)


    def test_status_is_rejected(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "rejected",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

    def test_status_is_resolved(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "resolved",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

    def test_get_all_incident(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)


        response = self.tester.get(
            '/api/v1/incidents/', content_type='application/json', headers={'Authorization': f'Bearer {token}'}
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_no_incident(self):
        reply = self.login_user()
        token = reply['token']
        response = self.tester.get(
            '/api/v1/incidents/', content_type='application/json', headers={'Authorization': f'Bearer {token}'}
        )
        self.assertEqual(response.status_code, 404)


    def test_get_unique_incident(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "under_investigation",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        response = self.tester.get(
            '/api/v1/incidents/1', content_type='application/json', headers={'Authorization': f'Bearer {token}'}
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_id(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "under_investigation",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        response = self.tester.get(
            '/api/v1/incidents/2', content_type='application/json', headers={'Authorization': f'Bearer {token}'}
        )
        print(response.data)
        self.assertEqual(response.status_code, 404)


    def test_no_incident_yet(self):
        reply = self.login_user()
        token = reply['token']
        response = self.tester.get(
            '/api/v1/incidents/1', content_type='application/json', headers={'Authorization': f'Bearer {token}'}
        )
        self.assertEqual(response.status_code, 404)


    def test_update_location(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "under_investigation",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_location = { "location": "2125157"}

        response = self.tester.patch(
            '/api/v1/incidents/1/location', content_type='application/json',
            data = json.dumps(update_location), headers = {'Authorization':f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["message"], "location updated successfully")
        self.assertEqual(response.status_code, 200)

    def no_incident_for_locatiion(self):
        response = self.tester.get(
            '/api/v1/incidents/1/location', content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)

    def test_update_location_is_empty(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "under_investigation",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_location = { "location": ""}

        response = self.tester.patch(
            '/api/v1/incidents/1/location', content_type='application/json',
            data = json.dumps(update_location), headers = {'Authorization':f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["error"], "location field can not be left empty and should be a string")
        self.assertEqual(response.status_code, 400)

    def test_update_location_is_not_string(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "under_investigation",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_location = { "location": False}

        response = self.tester.patch(
            '/api/v1/incidents/1/location', content_type='application/json',
            data = json.dumps(update_location), headers = {'Authorization':f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["error"], "location field can not be left empty and should be a string")
        self.assertEqual(response.status_code, 400)

    def test_update_comment(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "under_investigation",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_comment = { "comment": "Rejected red-flag"}

        response = self.tester.patch(
            '/api/v1/incidents/1/comment', content_type='application/json',
            data = json.dumps(update_comment), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["message"], "comment updated successfully")
        self.assertEqual(response.status_code, 200)

    def test_no_incident_for_comment(self):
        reply = self.login_user()
        token = reply['token']
        response = self.tester.patch(
            '/api/v1/incidents/1/comment', content_type='application/json', headers={'Authorization': f'Bearer {token}'}
        )
        self.assertEqual(response.status_code, 400)

    def test_update_comment_is_empty(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "under_investigation",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_comment = { "comment": ""}

        response = self.tester.patch(
            '/api/v1/incidents/1/comment', content_type='application/json',
            data = json.dumps(update_comment), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["error"], "comment field can not be left empty and should be a string")
        self.assertEqual(response.status_code, 400)

    def test_update_comment_is_not_string(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "under_investigation",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_comment = { "comment": False}

        response = self.tester.patch(
            '/api/v1/incidents/1/comment', content_type='application/json',
            data = json.dumps(update_comment), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["error"], "comment field can not be left empty and should be a string")
        self.assertEqual(response.status_code, 400)

#     def test_update_comment_when_no_red_flag(self):
#         response = self.tester.patch(
#             '/api/v1/incidents/1/comment', content_type='application/json'
#         )
#         self.assertEqual(response.status_code, 400)

    def test_delete_a_redflag(self):
        reply = self.login_user()
        token = reply['token']
        report = {
            "comment": "No comment",
            "createdby": 1,
            "createdon": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "inctype": "red-flag",
            "location": "101010",
            "status": "under_investigation",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report), headers={'Authorization': f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        response = self.tester.delete(
            '/api/v1/incidents/1', content_type='application/json',
            data = json.dumps(report), headers = {'Authorization':f'Bearer {token}'}
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["message"], "incident deleted")
        self.assertEqual(response.status_code, 200)




    def tearDown(self):
        self.db.drop_table('incidents')

