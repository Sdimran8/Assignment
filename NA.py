# import requests

# api_key = "c72459652bb44caba49f58d8399447a0"

# def news():
#     main_url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+api_key
#     new = requests.get(main_url).json()
#     article = new['articles']
#     # print(article)

#     news_article = []
#     for i in article:
#         news_article.append(i['title'])
#         # print(news_article)

#     for j in range(5):
#         print(j+1,news_article[j])    

# news()

