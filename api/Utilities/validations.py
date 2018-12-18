from api.Models.Users import User
import re
import os
class Validations:
    '''Class handles all user validations when signup'''
    def __init__(self, firstname, lastname, othernames, email, phone_number, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
    
    def validate_firstname(self):
        '''Method validates the firstname attribute.
        :return:
        a error message
        '''
        if not self.firstname or self.firstname == "" or not type(self.firstname) == str:
            return {
                'status': 400,
                'error': 'Firstname field can not be left empty and should be a string'
            }

    def validate_lastname(self):
        '''Method validates the lastname attribute.
        :return:
        a error message
        '''
        if not self.lastname or self.lastname == "" or not type(self.lastname) == str:
            return {
                'status': 400,
                'error': 'Lastname field can not be left empty and should be a string'
            }
        

    def validate_othernames(self):
        '''Method validates the othernames attribute.
        :return:
        a error message
        '''
        if not self.othernames or self.othernames == "" or not type(self.othernames) == str:
            return {
                'status': 400,
                'error': 'othernames field can not be left empty and should be a string'
            }
        
    
    def validate_email(self):
        '''Method validates the email attribute.
        :return:
        a error message
        '''
        if not self.email or not type(self.email) == str or self.email == "" or \
        not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return {
                'status': 400,
                'error': 'Email field can not be left empty, is invalid(eg: example@example.com) and should be a string'
            }
        

    def validate_phone_number(self):
        '''Method validates the phone_number attribute.
        :return:
        a error message
        '''
        if not self.phone_number or self.phone_number == "" or not type(self.phone_number) == str:
            return {
                'status': 400,
                'error': 'phone_number field can not be left empty and should be a string!'
            }
        

    def validate_username(self):
        '''Method validates the username attribute.
        :return:
        a error message
        '''
        if not self.username or self.username == "" or not type(self.username) == str:
            return {
                'status': 400,
                'error': 'Username field can not be left empty and should be a string'
            }
    
    def validate_password(self):
        '''Method validates the password attribute.
        :return:
        a error message
        '''
        if not self.password or self.password == "" or not type(self.password) == str:
            return {
                'status': 400,
                'error': 'Password field can not be left empty and should be a string'
            }
        
    @staticmethod
    def empty_user(data):
        ''' Function enables to check if the accounts list is empty
        :param:
        data - holds information of the accounts list in the User class
        :returns:
        a error message.
        '''
        if len(data) == 0:
            return {
                'status': 404,
                'error': 'There are no user yet!'
            }

    @staticmethod
    def validate_signup(username, email):
        ''' Function enables to check if the user exist in the account list
        :param:
        username - holds the username entered by a user and check if it matches any username in the accounts list
        email - holds the email entered by a user and check if it matches any email in the accounts list
        both :returns:
        a error message.
        '''

        for user in User.accounts:
            if user["username"] == username:
                return {
                    'status': 400,
                    'error': 'username already taken'
                }
            elif user["email"] == email:
                return {
                    'status': 400,
                    'error': 'email already existed'
                }

class Login_validation:
    '''Class handles all user validations when login'''
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_username(self):
        '''Method validates the firstname attribute.
        :return:
        a error message
        '''
        if not self.username or self.username == "" or not type(self.username) == str:
            return {
                'status': 400,
                'error': 'Username field can not be left empty and should be a string'
            }

    def validate_password(self):
        '''Method validates the password attribute.
        :return:
        a error message
        '''
        if not self.password or self.password == "" or not type(self.password) == str:
            return {
                'status': 400,
                'error': 'Password field can not be left empty and should be a string'
            }
    
class Incident_validation:
    '''Class handles all incident validations'''
    def __init__(self, createdBy, incType, location, status, image, video, comment):
        self.createdBy = createdBy
        self.incType = incType
        self.location = location
        self.status = status
        self.image = image
        self.video = video
        self.comment = comment

    def validate_createdBy(self):
        '''Method validates the createdBy attribute.
        :return:
        a error message
        '''
        if not self.createdBy or not isinstance(self.createdBy, int):
            return {
                'status': 400,
                'error': 'createdBy field can not be left empty and should be an integer'
                }
        
    def validate_incType(self):
        '''Method validates the incType attribute.
        :return:
        a error message
        '''
        if not self.incType or self.incType == "" or not self.incType == "intervention" \
        and not self.incType == "red-flag" or not isinstance(self.incType, str):
            return {
                'status': 400,
                'error': 'incType field can not be left empty, it should be eg: red-flag or intervention\
                and should be a string'
            }
    
    def validate_location(self):
        '''Method validates the location attribute.
        :return:
        a error message
        '''
        if not self.location or self.location == "" or not isinstance(self.location, str):
            return {
                'status': 400,
                'error': 'location field can not be left empty and should be a string'
            }
    
    def validate_status(self):
        '''Method validates the status attribute.
        :return:
        a error message
        '''
        if not self.status or self.status == "" or not self.status == "draft" \
        and not self.status == "under_investigation" and not self.status== "rejected"\
         and not self.status=="resolved" or not isinstance(self.status, str):
            return {
                'status': 400,
                'error':'status field can not be left empty, it should be eg: draft, resolved, under_investigation or rejected \
                and should be a string'
            }

    def validate_image(self):
        '''Method validates the image attribute.
        :return:
        a error message
        '''
        extensions = [".jpg", ".png"]
        details = os.path.splitext(self.image)
        if details[1] not in extensions:
            return {
                'status': 400,
                'error': 'image has an invalid format(eg: image.png  or image.jpg'
            }

    def validate_video(self):
        '''Method validates the video attribute.
        :return:
        a error message
        '''
        extensions = [".mp4", ".avi"]
        details = os.path.splitext(self.video)
        if details[1] not in extensions:
            return {
                'status': 400,
                'error': 'video has an invalid format(eg: video.mp4  or video.avi)'
        }
    
    def validate_comment(self):
        '''Method validates the comment attribute.
        :return:
        a error message
        '''
        if not self.comment or self.comment == "" or not isinstance(self.comment, str):
            return {
                'status': 400,
                'error': 'comment field can not be left empty and should be a string'
            }
    
    @staticmethod
    def empty_incident(data):
        ''' Function enables to check if the reports list is empty
        :param:
        data - holds information of the reports list in the User class
        :returns:
        a error message.
        '''
        if len(data) == 0:
            return {
                'status': 400,
                'error': 'There are no incident yet!'
            }

    @staticmethod
    def validate_red_flag_comment(comment):
        ''' Function enables to validate comment
        :param:
        comment - holds the comment information entered by a user before update it
        :returns:
        a error message.
        '''
        if not comment or comment == "" or not isinstance(comment, str) :
            return {
                'status': 400,
                'error': 'comment field can not be left empty and should be a string'
            }
            
    @staticmethod
    def validate_red_flag_location(location):
        ''' Function enables to validate location
        :param:
        location - holds the location information entered by a user before update it
        :returns:
        a error message.
        '''
        if not location or location == "" or not isinstance(location, str):
            return {
                'status': 400,
                'error': 'location field can not be left empty and should be a string'
            }

