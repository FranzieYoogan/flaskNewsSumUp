import json
from flask import Flask, render_template, request
from newspaper import Article
import requests 
from lxml_html_clean import Cleaner
from bs4 import BeautifulSoup 

app = Flask(__name__)


@app.route('/')
def home():
  
  response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=019145f2a2e1437980e54a6154024cbc")

  data = response.text

  parseJson = json.loads(data)

  dataArticle = parseJson['articles']
  print(dataArticle)


  return render_template('home.htm',dataArticle = dataArticle)

  



@app.route('/search', methods=['GET','POST'])
def Search():
  if request.method == 'POST':
    
    url = request.form.get('url') 
          #For different language newspaper refer above table
    toi_article = Article(url, language="en") # en for English
    
    #To download the article
    toi_article.download()
    
    #To parse the article
    toi_article.parse()
    
    #To perform natural language processing ie..nlp
    toi_article.nlp()
    summary = toi_article.summary
    title = toi_article.title


    return render_template('search.htm', summary = summary, title = title)
    
  return render_template('search.htm')



if __name__ == '__main__':  
   app.run(debug=True)

