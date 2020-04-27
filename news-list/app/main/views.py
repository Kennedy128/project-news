from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles



#Views 
@main.route('/')
def index():
    general = get_sources('general')
    business = get_sources('business')
    technology = get_sources('technology')
    technology = get_sources('general')
    sport = get_sources('general')

    title = 'News-app'
    

    return render_template('index.html', title = title, general = general, business = business, technology= technology  )


@main.route('/source/<id>')
def articles(id):
    news_articles = get_articles(id)

    title = f'{id}'

    return render_template('source.html', title = title, news_articles = news_articles)