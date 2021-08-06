from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/post')
def postrender():
    return 'Post'


