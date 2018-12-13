from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from api.Controllers.user_controller import signup, login, promote_user_as_admin, get_all_users
from api.Controllers.incident_controller import create_incident, get_all_incidents, get_unique_red_flag,\
update_red_flag_com, update_red_flag_loc, update_red_flag_com, delete_red_flag

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'SECretK1ey'

@app.route('/')
def test_route():
    return "welcome to iReporter"

@app.route('/api/v1/signup/', methods=['POST'])
def signUp():
    response = signup()
    return response
    
@app.route('/api/v1/login/', methods=['POST']) 
def user_login():
    response = login()
    return response

@app.route('/api/v1/welcome')
@jwt_required
def welcome():
    username = get_jwt_identity()
    return jsonify({
        'status': 200,
        'message': f'{username} thanks for using iReporter Api'
    }), 200

@app.route('/api/v1/user/promote/<int:user_id>', methods=['PATCH'])
def promote_user(user_id):
    response = promote_user_as_admin(user_id)
    return response

@app.route('/api/v1/users/', methods=['GET']) 
def get_users():
   response = get_all_users()
   return response


@app.route('/api/v1/incident/', methods=['POST'])
def create_report():
    response = create_incident()
    return response


@app.route('/api/v1/incidents/', methods=['GET'])
def get_incidents():
    response = get_all_incidents()
    return response

@app.route('/api/v1/incidents/<int:incident_id>', methods=['GET'])
def get_red_flag(incident_id):
    response = get_unique_red_flag(incident_id)
    return response

@app.route('/api/v1/incidents/<int:incident_id>/location', methods=['PATCH'])
def update_red_flag_location(incident_id):
    response = update_red_flag_loc(incident_id)
    return response

@app.route('/api/v1/incidents/<int:incident_id>/comment', methods=['PATCH'])
def update_red_flag_comment(incident_id):
    response = update_red_flag_com(incident_id)
    return response

@app.route('/api/v1/incidents/<int:incident_id>', methods=['DELETE'])
def delete_a_unique_redflag(incident_id):
    response = delete_red_flag(incident_id)
    return response

