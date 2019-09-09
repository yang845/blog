#encoding:utf8
from . import v1
from app.models import Friend
from flask import request,url_for,jsonify,make_response
from app import db

@v1.route('/friends/')
def get_friends():
    friends = Friend.query.order_by(Friend.timestamp.asc()).all()

    return jsonify({
        'friends': [friend.to_json() for friend in friends if friend.display]
    })

@v1.route('/friend/',methods=['POST'])
def new_friend():
    friend = Friend.from_json(request.json)
    db.session.add(friend)
    db.session.commit()
    result_text = {"status": 1}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response