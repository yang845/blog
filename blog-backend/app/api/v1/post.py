#encoding:utf8
from . import v1
from flask import jsonify,request,url_for
from app.models import Post
from app import db
import math

@v1.route('/post/<int:id>')
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json())

@v1.route('/archives/')
def archives():
    posts = Post.query.order_by(Post.timestamp.desc())
    print(posts)
    return jsonify({
        'posts': [post.to_json() for post in posts]
    })

@v1.route('/posts/')
def get_posts():
    page = request.args.get('page', 1, type=int)
    # print(request.args)
    per_page = request.args.get('size', 12, type=int)
    pagination = Post.query.paginate(
        page, per_page=per_page,
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_posts', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_posts', page=page + 1)
    page_list = []
    page_count = math.ceil(pagination.total / per_page)
    for p in range(1, page_count +  1):
        page_list.append(p)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev_url': prev,
        'next_url': next,
        'page_list': page_list,
        'curr_page': pagination.page,
        'count': pagination.total,
        'page_count': page_count
    })

@v1.route('/likes/')
def likes():
    id = request.args.get('id', type=int)
    post = Post.query.filter_by(id=id).first()
    post.likes = post.likes + 1
    db.session.add(post)
    db.session.commit()
    return jsonify({
        'status': 1
    })


