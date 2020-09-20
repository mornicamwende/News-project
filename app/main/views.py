from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_articles


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_categories = get_sources('general')
    # business_category = get_sources('business')
    # entertainment_categories = get_sources('entertainment')
    # sports_categories = get_sources('sports')
    # technology_categories = get_sources('technology')
    # science_category = get_sources('science')
    # health_category = get_sources('health')

    title = 'The Worlds Daily Dose'
    return render_template('index.html',title = title, general = general_categories)

@main.route('/newsarticle/<id>')
def newsarticle(id):

    '''
    View article page function that returns the article details page and its data
    '''
    articles_items = get_articles(id)
    title = f'{id} | News Articles'
    return render_template('newsarticle.html',title = title,articles = articles_items)