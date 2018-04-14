# coding=utf-8
from flask import jsonify


def index():
    """ Get all data

    :return: JSON response
    """

    try:
        response = {
            "success": True,
            "message": "Fetch all data successfully",
            "data": []
        }

        return jsonify(response), 200

    except Exception as ex:
        response = {
            'success': False,
            'message': 'Something went wrong on fetching posts',
            'error': str(ex)
        }

        return jsonify(response), 500


def create():
    """ Create new records

    :return: JSON response
    """

    try:
        response = {
            'success': True,
            'message': 'Data added successfully',
            'data': []
        }

        return jsonify(response), 201

    except Exception as ex:
        response = {
            'success': False,
            'message': 'Something went wrong on creating posts',
            'error': str(ex)
        }

        return jsonify(response), 500


def get(id):
    """ Get single data by ID

    :param id: str
    :return: JSON response
    """

    try:
        response = {
            "success": True,
            "message": "Data fetch successfully",
            "data": []
        }

        return jsonify(response), 200

    except Exception as ex:
        response = {
            'success': False,
            'message': 'Something went wrong on fetching single post',
            'error': str(ex)
        }

        return jsonify(response), 500


def update(id):
    """Record update

    :param id: str
    :return: JSON response
    """

    try:
        response = {
            "success": True,
            "message": "Data successfully updated",
            "data": []
        }

        return jsonify(response), 201

    except Exception as ex:
        response = {
            'success': False,
            'message': 'Something went wrong on updating post',
            'error': str(ex)
        }

        return jsonify(response), 500


def delete(id):
    """Delete record by ID

    :param id: str
    :return: JSON response
    """

    try:
        response = {
            "success": True,
            "message": "Data successfully deleted",
            "data": []
        }

        return jsonify(response), 201

    except Exception as ex:
        response = {
            'success': False,
            'message': 'Something went wrong on updating post',
            'error': str(ex)
        }

        return jsonify(response), 500
