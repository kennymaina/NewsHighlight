from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources

from ..models import Source



# @main.route('/source/<id>')
# def articles(id):
#     """
#     View root page function that returns the index page and its data
#     """

#     articleSource=get_articles(id)
#     title = 'Article Sources-catchup on whats latest'
#     print(articleSource)
#     return render_template('index.html',title=title,articles=articleSource)

@main.route('/')
def index():
    """
    View source page function that returns the  sources and their details
    """
    news_sources= get_sources('general')
    return render_template('index.html',general=news_sources)