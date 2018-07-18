#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from flask import Blueprint, render_template, abort
from simpledu.models import User, Course

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/<name>')
def user_index(name):
    author = User.query.filter_by(username=name).first()
    if author is None:
        abort(404)
    courses = Course.query.filter_by(author_id=author.id).all()
    return render_template('user.html', name=name, author=author, courses=courses)
