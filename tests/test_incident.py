import unittest
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api.Views.routes import app
from api.Models.Incidents import Incident

class Test_Incident(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client()

    def test_create_incident(self):
        report = {
            "comment": "No comment",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

    def test_create_comment_is_empty(self):
        report = {
            "comment": "",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("comment field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)
    
    def test_create_createdBy_is_not_an_integer(self):
        report = {
            "comment": "No comment for now",
            "createdBy": False,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("createdBy field can not be left empty and should be an integer", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_create_createdBy_is_empty(self):
        report = {
            "comment": "No comment for now",
            "createdBy": "",
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("createdBy field can not be left empty and should be an integer", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_create_location_is_not_a_string(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": 101010,
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("location field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_create_location_is_empty(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("location field can not be left empty and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_image_has_an_invalid_format(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.gif",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("image has an invalid format(eg: image.png  or image.jpg", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_image_has_an_empty_name(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": ".jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("image has an invalid format(eg: image.png  or image.jpg", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_image_has_a_invalid_input(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": 1212546,
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("Something went wrong with your inputs", reply['error'])
        self.assertEqual(response.status_code, 400)


    def test_video_has_invalid_format(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "img.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.xls"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("video has an invalid format(eg: video.mp4  or video.avi)", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_video_has_an_invalid_name(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": ".avi"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("video has an invalid format(eg: video.mp4  or video.avi)", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_video_has_invalid_input(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": True
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("Something went wrong with your inputs", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_incType_is_empty(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("incType field can not be left empty, it should be eg: red-flag or intervention\
                and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_incType_is_not_a_string(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": False,
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("incType field can not be left empty, it should be eg: red-flag or intervention\
                and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)
    
    def test_incType_is_not_red_flag_or_intervention(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "crime",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("incType field can not be left empty, it should be eg: red-flag or intervention\
                and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_incType_is_intervention(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "intervention",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("intervention has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

    def test_incType_is_red_flag(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)


    def test_status_is_not_a_string(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": 1214,
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("status field can not be left empty, it should be eg: draft, resolved, under_investigation or rejected \
                and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_status_is_empty(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("status field can not be left empty, it should be eg: draft, resolved, under_investigation or rejected \
                and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)
    
    def test_status_is_string_but_invalid(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "over",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("status field can not be left empty, it should be eg: draft, resolved, under_investigation or rejected \
                and should be a string", reply['error'])
        self.assertEqual(response.status_code, 400)

    def test_status_is_draft(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "draft",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

    def test_status_is_under_investigation(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "under_investigation",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

    def test_status_is_rejected(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "rejected",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

    def test_status_is_resolved(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "resolved",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

    def test_get_all_incident(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "resolved",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        response = self.tester.get(
            '/api/v1/incidents/', content_type='application/json'
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_unique_incident(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "resolved",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        response = self.tester.get(
            '/api/v1/incidents/1', content_type='application/json'
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)


    def test_update_location(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "resolved",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_location = { "location": "2125157"}

        response = self.tester.patch(
            '/api/v1/incidents/1/location', content_type='application/json',
            data = json.dumps(update_location)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["message"], "location updated successfully")
        self.assertEqual(response.status_code, 200)

    def test_update_location_is_empty(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "resolved",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_location = { "location": ""}

        response = self.tester.patch(
            '/api/v1/incidents/1/location', content_type='application/json',
            data = json.dumps(update_location)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["error"], "location field can not be left empty and should be a string")
        self.assertEqual(response.status_code, 400)

    def test_update_location_is_not_string(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "resolved",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_location = { "location": True}

        response = self.tester.patch(
            '/api/v1/incidents/1/location', content_type='application/json',
            data = json.dumps(update_location)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["error"], "location field can not be left empty and should be a string")
        self.assertEqual(response.status_code, 400)

    def test_update_comment(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "resolved",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_comment = { "comment": "Rejected red-flag"}

        response = self.tester.patch(
            '/api/v1/incidents/1/comment', content_type='application/json',
            data = json.dumps(update_comment)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["message"], "comment updated successfully")
        self.assertEqual(response.status_code, 200)

    def test_update_comment_is_empty(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "resolved",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_comment = { "comment": ""}

        response = self.tester.patch(
            '/api/v1/incidents/1/comment', content_type='application/json',
            data = json.dumps(update_comment)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["error"], "comment field can not be left empty and should be a string")
        self.assertEqual(response.status_code, 400)

    def test_update_comment_is_not_string(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "resolved",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        update_comment = { "comment": 11234}

        response = self.tester.patch(
            '/api/v1/incidents/1/comment', content_type='application/json',
            data = json.dumps(update_comment)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["error"], "comment field can not be left empty and should be a string")
        self.assertEqual(response.status_code, 400)

    def test_update_comment_when_no_red_flag(self):

        response = self.tester.patch(
            '/api/v1/incidents/1/comment', content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_a_redflag(self):
        report = {
            "comment": "No comment for now",
            "createdBy": 1,
            "createdOn": "Thu, 13 Dec 2018 08:33:24 GMT",
            "image": "image.jpg",
            "incType": "red-flag",
            "incident_id": 1,
            "location": "101010",
            "status": "resolved",
            "video": "video.mp4"
        }

        response = self.tester.post(
            '/api/v1/incident/', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn("red-flag has been created successfuly", reply['message'])
        self.assertEqual(response.status_code, 201)

        response = self.tester.delete(
            '/api/v1/incidents/1', content_type='application/json',
            data = json.dumps(report)
        )
        reply = json.loads(response.data.decode())
        print(response.data)
        self.assertIn(reply["message"], "incident deleted")
        self.assertEqual(response.status_code, 200)



    def tearDown(self):
        Incident.reports.clear()

