# coding=utf-8
from flask import jsonify, request
from ..models import db, User
from pprint import pprint


def get_all_user():
    try:
        results = User.query.all()
        data = [result.as_dict() for result in results]

        return jsonify({"success": True, "message": "Fetch all users successfully", "data": data}), 200

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on fetching users',
            'error': str(ex)
        }

        return jsonify(response), 500


def add_user():
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
            pprint(user_obj)

            return jsonify({'success': True, 'message': 'User added successfully', 'data': user_obj.as_dict()}), 201

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on creating user',
            'error': str(ex)
        }

        return jsonify(response), 500


def get_user(id):
    try:
        result = User.query.get(id)
        if result:
            del result.as_dict()['password']
            return jsonify({"success": True, "message": "Fetched user successfully", "data": result}), 200
        else:
            return jsonify({"success": False, "message": "No user found with this {0}".format(id)}), 404

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on fetching single user',
            'error': str(ex)
        }

        return jsonify(response), 500


def update_user(id):
    try:
        body = request.json
        result = User.query.get(id)

        if result:
            result.full_name = body.get('full_name')
            result.email = body.get('email')
            db.session.commit()
            del result['password']

            return jsonify({"success": True, "message": "User updated successfully", "data": result.as_dict()}), 201

        else:
            return jsonify({"success": False, "message": "No user found with this {0}".format(id)}), 404

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on updating user',
            'error': str(ex)
        }

        return jsonify(response), 500


def delete_user(id):
    try:
        result = User.query.get(id)

        if result:
            db.session.delete(result)
            db.session.commit()

            return jsonify({"success": True, "message": "User successfully deleted", "data": result.as_dict()}), 201

        else:
            return jsonify({"success": False, "message": "No user found with this {0}".format(id)}), 404

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on deleting user',
            'error': str(ex)
        }

        return jsonify(response), 500
