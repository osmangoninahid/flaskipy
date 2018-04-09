# coding=utf-8
from flask import jsonify, request
from pprint import pprint


def index():
    try:
        response = {
            'success': True,
            'message': 'Hello there!',
            'data': []
        }

        return jsonify(response), 200

    except Exception as ex:
        pprint(ex)


def create():
    try:
        response = {
            'success': True,
            'message': 'Post created!',
            'data': request.json
        }

        return jsonify(response), 201

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': str(ex)
        }

        return jsonify(response), 500


def get(id):
    try:
        response = {
            'success': True,
            'message': 'Hello there id: '+id,
            'data': []
        }

        return jsonify(response), 200

    except Exception as ex:
        pprint(ex)


def update(id):
    try:
        response = {
            'success': True,
            'message': 'Post updated id: '+id,
            'data': request.json
        }

        return jsonify(response), 201

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': str(ex)
        }

        return jsonify(response), 500


def delete(id):
    try:
        response = {
            'success': True,
            'message': 'Post deleted id: '+id,
            'data': []
        }

        return jsonify(response), 201

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': str(ex)
        }

        return jsonify(response), 500