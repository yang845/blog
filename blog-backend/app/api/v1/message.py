#encoding:utf8
from . import v1
from app.models import Message
from flask import url_for,request,jsonify
from app import db
from random import randint
import math

@v1.route('/messages/')
def get_messages():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('size', 12, type=int)
    pagination = Message.query.filter_by().order_by(Message.timestamp.desc()).paginate(
        page=page, per_page=per_page,
        error_out=False)
    messages = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_messages', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_messages', page=page + 1)
    page_list = []
    page_count = math.ceil(pagination.total / per_page)
    for p in range(1, page_count + 1):
        page_list.append(p)
    return jsonify({
        'messages': [message.to_json() for message in messages if message.display],
        'prev': prev,
        'next': next,
        'page_list': page_list,
        'curr_page': pagination.page,
        'count': pagination.total,
        'page_count': page_count
    })

@v1.route('/message/',methods=['POST'])
def new_message():
    message = Message.from_json(request.json)
    head_img = url_for('static', filename='gravatar/img' + str(randint(1, 9)) + '.jpg')
    message.img_url = head_img
    db.session.add(message)
    db.session.commit()
    return jsonify({
        'status': 1
    })
