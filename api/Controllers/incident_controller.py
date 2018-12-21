from flask import Flask, jsonify, request
from db import DatabaseConnection
from api.Models.Incidents import Incident
from api.Utilities.validations import *
import datetime

db = DatabaseConnection()

def create_incident():
    try:
        data = request.get_json()
        #incident_id = len(Incident.reports)+1
        createdon = data.get("createdon")
        createdby = data.get("createdby")
        inctype = data.get("inctype")
        location = data.get("location")
        status = data.get("status")
        image = data.get("image")
        video = data.get("video")
        comment = data.get("comment")

        # validation
        validator = Incident_validation(createdby, inctype, location, status, image, video, comment)
        invalid_createdby = validator.validate_createdby()
        invalid_inctype = validator.validate_inctype()
        invalid_location = validator.validate_location()
        invalid_status = validator.validate_status()
        invalid_image = validator.validate_image()
        invalid_video = validator.validate_video()
        invalid_comment = validator.validate_comment()
        

        if not invalid_createdby:
            if not invalid_inctype:
                if not invalid_location:
                    if not invalid_status:
                        if not invalid_image:
                            if not invalid_video:
                                if not invalid_comment:
                                        # report = Incident(incident_id, createdon, createdby, inctype, location, status, image, video, comment)
                                        db.insert_incident(createdon, createdby, inctype, location, status, image, video, comment)
                                        # Incident.reports.append(report.__dict__)
                                        return jsonify({
                                            "status": 201,
                                            # "data": report.__dict__,
                                            "message": f"{inctype} has been created successfuly"
                                        }), 201
                                return jsonify(invalid_comment), 400
                            return jsonify(invalid_video), 400
                        return jsonify(invalid_image), 400
                    return jsonify(invalid_status), 400
                return jsonify(invalid_location), 400
            return jsonify(invalid_inctype), 400
        return jsonify(invalid_createdby), 400

    except Exception:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong with your inputs'
        }), 400

def get_all_incidents():
    if not db.query_all("incidents"):
        return jsonify({
            'status': 400,
            'error': 'There are incident yet'
        })

    incidents = db.query_all("incidents")
    for incident in incidents:
        incident_dict = {
            "incident_id": incident["incident_id"],
            "createdon": incident["createdon"],
            "createdby": incident["createdby"],
            "inctype": incident["inctype"],
            "location": incident["location"],
            "status": incident["status"],
            "image": incident["image"],
            "video": incident["video"],
            "comment": incident["comment"]
        }
        Incident.reports.append(incident_dict)

    return jsonify({
        'status': 200,
        'data': Incident.reports,
        'message': 'Incidents Fetched'
    })

  

def get_unique_red_flag(incident_id):
    try:
            
        if not db.query_one(incident_id):
            return jsonify({
            'status': 404,
            'error': 'Please red-flag does not exit or check your id'
        }), 404

        incidents = db.query_one(incident_id)
        for red_flag in incidents:
            red_flag_dic = {
                "incident_id": red_flag["incident_id"],
                "createdon": red_flag["createdon"],
                "createdby": red_flag["createdby"],
                "inctype": red_flag["inctype"],
                "location": red_flag["location"],
                "status": red_flag["status"],
                "image": red_flag["image"],
                "video": red_flag["video"],
                "comment": red_flag["comment"]
            }

        return jsonify({
            'status': 200,
            'data': red_flag_dic,
            'message': 'Red-Flag Fetched'
        }), 200

    except IndexError:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong'
        }), 400

    

def update_red_flag_loc(incident_id):
    try:
#         validator = Incident_validation.empty_incident(Incident.reports)
#         if not validator:
        data = request.get_json()
        location = data.get("location")
        val = Incident_validation.validate_red_flag_location(location)
        if not val:
            db.update("incidents", "location", location, "incident_id", incident_id)
            return jsonify({
                'status': 200,
                'message': 'location updated successfully'
            }), 200
        else:
            return jsonify(val), 400
        
#         else:
#             return jsonify(validator), 400
    except Exception:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong with your inputs or check your id in the URL'
        }), 400

def update_red_flag_com(incident_id):
    try:
        # validator = Incident_validation.empty_incident(Incident.reports)
        # if not validator:
        data = request.get_json()
        comment = data.get("comment")
        val = Incident_validation.validate_red_flag_comment(comment)
        if not val:
            db.update("incidents", "comment", comment, "incident_id", incident_id)
            return jsonify({
                'status': 200,
                'message': 'comment updated successfully'
            })
        else:
            return jsonify(val), 400
        # else:
        #     return jsonify(validator), 400
    except Exception:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong with your inputs or check your id in the URL'
        }), 400

def delete_red_flag(incident_id):
    try:
#         validator = Incident_validation.empty_incident(Incident.reports)
#         if not validator:
        # incident = next(incident for incident in Incident.reports if incident['incident_id'] == incident_id)
        db.delete("incidents", "incident_id", incident_id)
        return jsonify({
            'status': 200,
            'message': 'incident deleted'
        }), 200
        
#         else:
#             return jsonify(validator), 400
    except IndexError:
        return jsonify({
            'message': 'incident does not exit or check your id',
            'status': 404
        }), 404
        