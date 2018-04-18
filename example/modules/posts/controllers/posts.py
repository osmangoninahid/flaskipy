# coding=utf-8
from flask import jsonify, request, g
from ..models import db, Post
from pprint import pprint


def get_all_post():
    try:
        results = Post.query.all()
        data = [result.as_dict() for result in results]

        return jsonify({"success": True, "message": "Fetch all posts successfully", "data": data}), 200

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on fetching posts',
            'error': str(ex)
        }

        return jsonify(response), 500


def add_post():
    try:
        body = request.json
        print("Request body")
        pprint(body)

        if 'title' not in body or 'description' not in body or body.get('title') == '' or body.get('description') == '':
            return jsonify({"success": False, "message": "Required fields missing", "error": body}), 206

        else:
            post_obj = Post(
                title=body.get('title'),
                description=body.get('description')
            )
            db.session.add(post_obj)
            db.session.commit()
            pprint(post_obj)

            return jsonify({'success': True, 'message': 'Post added successfully', 'data': post_obj.as_dict()}), 201

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on creating post',
            'error': str(ex)
        }

        return jsonify(response), 500


def get_post(id):
    try:
        result = Post.query.get(id)
        if result:
            return jsonify({"success": True, "message": "Fetch post successfully", "data": result.as_dict()}), 200
        else:
            return jsonify({"success": False, "message": "No post found with this {0}".format(id)}), 404

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on fetching single post',
            'error': str(ex)
        }

        return jsonify(response), 500


def update_post(id):
    try:
        body = request.json
        result = Post.query.get(id)

        if result:
            result.title = body.get('title')
            result.description = body.get('description')
            db.session.commit()

            return jsonify({"success": True, "message": "Post successfully updated", "data": result.as_dict()}), 201

        else:
            return jsonify({"success": False, "message": "No post found with this {0}".format(id)}), 404

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on updating post',
            'error': str(ex)
        }

        return jsonify(response), 500


def delete_post(id):
    try:
        result = Post.query.get(id)

        if result:
            db.session.delete(result)
            db.session.commit()

            return jsonify({"success": True, "message": "Post successfully deleted", "data": result.as_dict()}), 201

        else:
            return jsonify({"success": False, "message": "No post found with this {0}".format(id)}), 404

    except Exception as ex:
        # error pretty print
        pprint(ex)
        response = {
            'success': False,
            'message': 'Something went wrong on updating post',
            'error': str(ex)
        }

        return jsonify(response), 500
