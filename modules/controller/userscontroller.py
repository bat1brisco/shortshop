import json

from functools import wraps
from flask import request, jsonify



from modules.helpers.database import db_session
from modules.helpers.statuscode import Status
from modules.helpers.serialize import *
from modules.model.usersmodel import *

"""
Create API function here
"""

def new_user():
    data = request.get_json()
    is_exist = Users.query.filter_by(email=data['email']).first()
    if not is_exist:
        user = Users(email=data['email'], pwd=data['pwd'])
        detail = UserDetails(
            fname           = data['fname'],
            lname           = data['lname'],
            mobile          = data['mobile'],
            telno           = data['telno'],
            address         = data['address'],
            profile_image   = data['profile_image'],
            details         = user,
            type_id         = data['type_id'],
            status_id       = data['status_id']
        )

        db_session.add(user)
        db_session.add(detail)

        try:
            db_session.commit()
            status = Status('200', 'Successfully Added New User!')
            return status.status_code()
        except:
            return Status('203', 'Something went wront, pls try again later!').status_code()
    else:
        return Status('204', 'User already exist!').status_code()

def get_single_user(id):
    user = Users.query.filter_by(user_id=id).first()
    data = serialize_data(user)

    if user:
        return Status('200', 'Ok', data).status_code()   
    else:
        return Status('404', 'User not found!').status_code()

def get_all_users():
    return ''

def get_user_details(id):
    detail = UserDetails.query.filter_by(detail_id=id).first()
    data = serialize_detail(detail)

    if detail:
        return Status('200', 'Ok', data).status_code()        
    else:
        return Status('404', 'Ok').status_code()

def update_user_details(id):
    return ''

def delete_user():
    return ''
