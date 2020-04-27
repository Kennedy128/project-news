import urllib.request, json 
from .models import Source, News

#Getting api key
api_key = None

#Getting the base url
source_base_url = None
category_base_url = None

def configure_requests(app):
    global api_key, source_base_url, category_base_url,article_base_url
    api_key = app.config['NEWS_API_KEY']
    source_base_url = app.config['SOURCE_NEWS_BASE_URL']
    category_base_url = app.config['CATEGORIZED_BASE_URL']    
    article_base_url = app.config['ARTICLE_BASE_URL']


def get_sources(category):
    source_url = category_base_url.format(category,api_key)
    print(source_url)
    with urllib.request.urlopen(source_url) as url:
        source_data = url.read()
        source_response = json.loads(source_data)
        

        source_results = None

        if source_response['sources']:
            source_results_list = source_response['sources']
            source_results = process_sources(source_results_list)
                  
    return source_results

def process_sources(source_list):
    sources_results = []
    for source_item in source_list:

        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get ('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Source(id,name,description,url,category,language,country)
        sources_results.append(source_object)


    return sources_results

def get_articles(id):
    print(id)
    article_url = article_base_url.format(id,api_key)
    print(article_url)
    with urllib.request.urlopen(article_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)
       

        article_result = None

        if article_response['articles']:
            article_result_list = article_response['articles']
            article_list = process_articles(article_result_list)
   
    return article_list


def process_articles(article_list):
    article_results = []

    for article_item in article_list:
        id = article_item.get("source['id']")
        name = article_item.get("source['name']")
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')
        
        article_object = News(id, name,author,title,description,url,urlToImage,publishedAt,content)
        article_results.append(article_object)

    return article_results
