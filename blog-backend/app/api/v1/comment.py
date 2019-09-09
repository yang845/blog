from . import v1
from flask import jsonify,url_for,request,current_app,make_response
from app.models import Post,Comment
from app import db
from random import randint
import math

@v1.route('/post/<int:id>/comments/')
def get_post_comments(id):
    post = Post.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('size', 12, type=int)
    pagination = post.comments.order_by(Comment.timestamp.desc()).paginate(
        page=page, per_page=per_page,
        error_out=False)
    comments = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_comments', id=id, page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_comments', id=id, page=page + 1)
    page_list = []
    page_count = math.ceil(pagination.total / per_page)
    for p in range(1, page_count + 1):
        page_list.append(p)
    return jsonify({
        'comments': [comment.to_json() for comment in comments if comment.display],
        'prev': prev,
        'next': next,
        'page_list': page_list,
        'curr_page': pagination.page,
        'count': pagination.total,
        'page_count': page_count
    })

@v1.route('/post/<int:id>/comment/',methods=['POST'])
def new_comment(id):
    comment = Comment.from_json(request.json)
    comment.post_id = id
    head_img = url_for('static', filename='gravatar/img' + str(randint(1, 9)) + '.jpg')
    comment.img_url = head_img
    db.session.add(comment)
    db.session.commit()

    result_text = {"status": 1}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

