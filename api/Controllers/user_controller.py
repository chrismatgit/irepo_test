from flask import Flask, jsonify, request
from db import DatabaseConnection
from api.Models.Users import User
from api.Utilities.validations import *
from flask_jwt_extended import create_access_token
import datetime

db = DatabaseConnection()
def signup():
    # try:
    data = request.get_json()
    # user_id = len(User.accounts)+1
    firstname = data.get("firstname")
    lastname = data.get("lastname")
    othernames = data.get("othernames")
    email = data.get("email")
    phone_number = data.get("phone_number")
    username = data.get("username")
    password = data.get("password")
    registered = data.get("registered")
    isAdmin = data.get("isAdmin")

    # validations
    validator = Validations(firstname, lastname, othernames, email, phone_number, username, password)
    invalid_firstname = validator.validate_firstname()
    invalid_lastname = validator.validate_lastname()
    invalid_othernames = validator.validate_othernames()
    invalid_email = validator.validate_email()
    invalid_username = validator.validate_username()
    invalid_phone_number = validator.validate_phone_number()
    invalid_password = validator.validate_password()
    valid = Validations.validate_signup(validator)

    # account = User(firstname, lastname, othernames, email, phone_number, username, password, registered)

    if not valid:
        if not invalid_firstname:
            if not invalid_lastname:
                if not invalid_othernames:
                    if not invalid_email:
                        if not invalid_phone_number:
                            if not invalid_username:
                                if not invalid_password:

                                    #User.accounts.append(account.__dict__) 
                                    db.user_signup(firstname, lastname, othernames, email, phone_number, username, password, registered, isAdmin)                        
                                    return jsonify({
                                        "status": 201,
                                        "message": f"{firstname} has been created successfuly"
                                    }), 201
                                return jsonify(invalid_password), 400
                            return jsonify(invalid_username), 400
                        return jsonify(invalid_phone_number), 400
                    return jsonify(invalid_email), 400
                return jsonify(invalid_othernames), 400
            return jsonify(invalid_lastname), 400
        return jsonify(invalid_firstname), 400
    return jsonify(valid), 400

    # except Exception:
    #     return jsonify({
    #         'status': 400,
    #         'error': 'Something went wrong with your inputs'
    #     }), 400


def login():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        validator = Login_validation(username, password)
        invalid_username = validator.validate_username()
        invalid_password = validator.validate_password()
            # valid = Validations.empty_user(validator)

            # if not valid:
        if not invalid_username:
            if not invalid_password:
                user = db.login(username)
                # for user in User.accounts:
                    # if user["username"]== username and user["password"] == password:
                if user != None:
                    if user["username"]== username and user["password"] == password:
                        expires = datetime.timedelta(days=1)
                        token = create_access_token(username, expires_delta=expires)
                        return jsonify({
                            "status": 200,
                            "token": token,
                            "message": f"{username} successfuly login"
                        }), 200
                    else:
                        return jsonify({
                            "status": 400,
                            "error": "Wrong username or password"
                        }), 400
                else:
                    return jsonify({
                        "status": 400,
                        "error": "Wrong username or password"
                    }), 400
            return jsonify(invalid_password), 400
        return jsonify(invalid_username), 400
    #     # return jsonify(valid), 400
    except Exception:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong with your inputs'
        }), 400


# def promote_user_as_admin(user_id):
#     try:
#         validator = Validations.empty_user(User.accounts)
#         if not validator:
#             for user in User.accounts:
#                 if user["user_id"] == user_id:
#                     user["isAdmin"] = True
#                     return jsonify({
#                         "status": 200,
#                         "data": user,
#                         "message": f"User with user_id {user_id} has been succesfuly promoted as an admin"
#                     }), 200
#                 else:
#                     return jsonify({
#                         "status": 404,
#                         "error": "User does not exist"
#                     }), 404
#         else:
#             return jsonify(validator), 404

#     except IndexError:
#         return jsonify({
#             'message': 'incident does not exit or check your id',
#             'status': 404
#         }), 404

def get_all_users():
    try: 
        if not db.query_all("users"):
            return jsonify({
                'status': 404,
                'error': 'There are no user yet'
            }), 404
        accounts = db.query_all("users")
        for account in accounts:
            account_dict = {
                "user_id": account["user_id"],
                "firstname": account["firstname"],
                "lastname": account["lastname"],
                "othernames": account["othernames"],
                "email": account["email"],
                "phone_number": account["phone_number"],
                "username": account["username"],
                "password": account["password"],
                "registered": account["registered"],
                "isadmin": account["isadmin"]
            }
            User.accounts.append(account_dict)
        return jsonify({
            'status': 200,
            'Data': User.accounts,
            'message': 'Accounts fetched'
        }), 200

    except Exception:
        return jsonify({
            'status': 400,
            'error': 'something went wrong'
        }), 400

