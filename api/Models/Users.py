class User(object):
    '''Class contains user's accounts'''
    accounts = []
    def __init__(self, user_id, firstname, lastname, othernames, email, phone_number, username, password, registered):
            self.user_id = user_id
            self.firstname = firstname
            self.lastname = lastname
            self.othernames = othernames
            self.email = email
            self.phone_number = phone_number
            self.username = username
            self.password = password
            self.registered = registered
            self.isAdmin = False