from flask import Flask, jsonify, Blueprint
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from api.Controllers.user_controller import signup, login, promote_user_as_admin, get_all_users
from api.Controllers.incident_controller import create_incident, get_all_incidents, get_unique_red_flag,\
update_red_flag_com, update_red_flag_loc, update_red_flag_com, delete_red_flag


bp = Blueprint('application', __name__)

@bp.route('/')
def test_route():
    '''Function returns a welcome message'''
    return "welcome to iReporter"

@bp.route('/signup/', methods=['POST'])
def signUp():
    '''Function adds the user to accounts list
    returns a success message and the user details'''
    response = signup()
    return response
    
@bp.route('/login/', methods=['POST']) 
def user_login():
    response = login()
    return response

@bp.route('/welcome')
@jwt_required
def welcome():
    username = get_jwt_identity()
    return jsonify({
        'status': 200,
        'message': f'{username} thanks for using iReporter Api'
    }), 200

@bp.route('/user/promote/<int:user_id>', methods=['PATCH'])
def promote_user(user_id):
    response = promote_user_as_admin(user_id)
    return response

@bp.route('/users/', methods=['GET']) 
def get_users():
   response = get_all_users()
   return response


@bp.route('/incident/', methods=['POST'])
def create_report():
    response = create_incident()
    return response


@bp.route('/incidents/', methods=['GET'])
def get_incidents():
    response = get_all_incidents()
    return response

@bp.route('/incidents/<int:incident_id>', methods=['GET'])
def get_red_flag(incident_id):
    response = get_unique_red_flag(incident_id)
    return response

@bp.route('/incidents/<int:incident_id>/location', methods=['PATCH'])
def update_red_flag_location(incident_id):
    response = update_red_flag_loc(incident_id)
    return response

@bp.route('/incidents/<int:incident_id>/comment', methods=['PATCH'])
def update_red_flag_comment(incident_id):
    response = update_red_flag_com(incident_id)
    return response

@bp.route('/incidents/<int:incident_id>', methods=['DELETE'])
def delete_a_unique_redflag(incident_id):
    response = delete_red_flag(incident_id)
    return response

@bp.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'issue': 'you have entered an unknown URL',
        'message': 'Please contact us for more details'
    })