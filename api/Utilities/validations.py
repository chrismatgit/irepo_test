from db import DatabaseConnection
from api.Models.Users import User
import re
import os

db = DatabaseConnection()

class Validations:
    def __init__(self, firstname, lastname, othernames, email, phone_number, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
    
    def validate_firstname(self):
        if not self.firstname or self.firstname == "" or not type(self.firstname) == str:
            return {
                'status': 400,
                'error': 'Firstname field can not be left empty and should be a string'
            }

    def validate_lastname(self):
        if not self.lastname or self.lastname == "" or not type(self.lastname) == str:
            return {
                'status': 400,
                'error': 'Lastname field can not be left empty and should be a string'
            }
        

    def validate_othernames(self):
        if not self.othernames or self.othernames == "" or not type(self.othernames) == str:
            return {
                'status': 400,
                'error': 'othernames field can not be left empty and should be a string'
            }
        
    
    def validate_email(self):
        if not self.email or not type(self.email) == str or self.email == "" or \
        not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return {
                'status': 400,
                'error': 'Email field can not be left empty, is invalid(eg: example@example.com) and should be a string'
            }
        

    def validate_phone_number(self):
        if not self.phone_number or self.phone_number == "" or not type(self.phone_number) == str:
            return {
                'status': 400,
                'error': 'phone_number field can not be left empty and should be a string!'
            }
        

    def validate_username(self):
        if not self.username or self.username == "" or not type(self.username) == str:
            return {
                'status': 400,
                'error': 'Username field can not be left empty and should be a string'
            }
    
    def validate_password(self):
        if not self.password or self.password == "" or not type(self.password) == str:
            return {
                'status': 400,
                'error': 'Password field can not be left empty and should be a string'
            }
        
#     @staticmethod
#     def empty_user(data):
#         if len(data) == 0:
#             return {
#                 'status': 404,
#                 'error': 'There are no user yet!'
#             }


    def validate_signup(self):
        username = db.check_username(self.username)
        email = db.check_email(self.email)

        if username != None:
            return {
                'status': 400,
                'error': 'username already taken'
            }
        if email != None:
            return {
                'status': 400,
                'error': 'email already existed'
            }


class Login_validation:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_username(self):
        if not self.username or self.username == "" or not type(self.username) == str:
            return {
                'status': 400,
                'error': 'Username field can not be left empty and should be a string'
            }

    def validate_password(self):
        if not self.password or self.password == "" or not type(self.password) == str:
            return {
                'status': 400,
                'error': 'Password field can not be left empty and should be a string'
            }
    
class Incident_validation:
    def __init__(self, createdby, inctype, location, status, image, video, comment):
        self.createdby = createdby
        self.inctype = inctype
        self.location = location
        self.status = status
        self.image = image
        self.video = video
        self.comment = comment
    def validate_createdby(self):
        if not self.createdby or not isinstance(self.createdby, int):
            return {
                'status': 400,
                'error': 'createdby field can not be left empty and should be an integer'
                }
        
    def validate_inctype(self):
        if not self.inctype or self.inctype == "" or not self.inctype == "intervention" \
        and not self.inctype == "red-flag" or not isinstance(self.inctype, str):
            return {
                'status': 400,
                'error': 'inctype field can not be left empty, it should be eg: red-flag or intervention\
                and should be a string'
            }
    
    def validate_location(self):
        if not self.location or self.location == "" or not isinstance(self.location, str):
            return {
                'status': 400,
                'error': 'location field can not be left empty and should be a string'
            }
    
    def validate_status(self):
        if not self.status or self.status == "" or not self.status == "draft" \
        and not self.status == "under_investigation" and not self.status== "rejected"\
         and not self.status=="resolved" or not isinstance(self.status, str):
            return {
                'status': 400,
                'error':'status field can not be left empty, it should be eg: draft, resolved, under_investigation or rejected \
                and should be a string'
            }

    def validate_image(self):
        extensions = [".jpg", ".png"]
        details = os.path.splitext(self.image)
        if details[1] not in extensions:
            return {
                'status': 400,
                'error': 'image has an invalid format(eg: image.png  or image.jpg'
            }

    def validate_video(self):
        extensions = [".mp4", ".avi"]
        details = os.path.splitext(self.video)
        if details[1] not in extensions:
            return {
                'status': 400,
                'error': 'video has an invalid format(eg: video.mp4  or video.avi)'
        }
    
    def validate_comment(self):
        if not self.comment or self.comment == "" or not isinstance(self.comment, str):
            return {
                'status': 400,
                'error': 'comment field can not be left empty and should be a string'
            }
    
#     @staticmethod
#     def empty_incident(data):
#         if len(data) == 0:
#             return {
#                 'status': 400,
#                 'error': 'There are no incident yet!'
#             }

    @staticmethod
    def validate_red_flag_comment(comment):
        if not comment or comment == "" or not isinstance(comment, str) :
            return {
                'status': 400,
                'error': 'comment field can not be left empty and should be a string'
            }
            
    @staticmethod
    def validate_red_flag_location(location):
        if not location or location == "" or not isinstance(location, str):
            return {
                'status': 400,
                'error': 'location field can not be left empty and should be a string'
            }

