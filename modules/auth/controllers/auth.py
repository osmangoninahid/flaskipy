# coding=utf-8
from flask import Flask, jsonify, request, g
from ...users.models import db, User
from pprint import pprint
import jwt


def login():
    try:
        body = request.json

        if 'user_name' not in body or 'password' not in body or body.get('user_name') == '' or body.get('password') == '':
            return jsonify({"success": False, "message": "user_name and/or password can not be empty", "error": body}), 206

        else:
            user = User.query.filter_by(user_name=body.get('user_name')).first()
            if user:
                if User.verify_password(user.password, body.get('password')):
                    token = jwt.encode({"user" : user.as_dict(),"exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=24*60*60)}, 'sEcReT', algorithm='HS256').decode('utf-8')
                    return jsonify({'success': True, 'message': 'Logged in successfully', 'token': token}), 200
                else:
                    return jsonify({'success': False, 'message': 'Pawword not matched'}), 200
            else:
                return jsonify({'success': False, 'message': 'No user found with this user_name'}), 200

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on login',
            'error': str(ex)
        }

        return jsonify(response), 500


def signup():
    try:
        body = request.json

        if 'user_name' not in body or 'password' not in body or body.get('user_name') == '' or body.get('password') == '':
            return jsonify({"success": False, "message": "Required fields can not be empty", "error": body}), 206

        else:
            user_obj = User(
                user_name=body.get('user_name'),
                password=body.get('password'),
                full_name = body.get('full_name'),
                email = body.get('email')
            )
            db.session.add(user_obj)
            db.session.commit()
            token = jwt.encode({"user" : user.as_dict(),"exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=24*60*60)}, 'sEcReT', algorithm='HS256').decode('utf-8')
            return jsonify({'success': True, 'message': 'User singed up successfully', 'data': user_obj.as_dict(), "token" : token}), 201

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on signing up user',
            'error': str(ex)
        }

        return jsonify(response), 500


def verify_auth_token(func):
    def authorization_checker(*args, **kwargs):
        # if authorization token is in headers
        if request.headers.get('Authorization', None):
            auth_user = jwt.decode(request.headers.get('Authorization'),'sEcReT', algorithm='HS256')

            if auth_user:
                g.auth_user = auth_user
                return True
            else:
                invalid_res = {
                    'success' : True,
                    'message': 'Sorry, you are not authorized to access this route!'
                }
                return jsonify(invalid_res), 401

        else:
            response = {
                'success' : False,
                'message': 'Sorry, authorization token is missing!'
            }
            return jsonify(response), 401

        return func(*args, **kwargs)

    return authorization_checker
