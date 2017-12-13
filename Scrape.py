import requests
from bs4 import BeautifulSoup as soup

#using request to get the page and assign to variable
getBUZZFEED = requests.get("http://www.buzzfeed.com/news")
BUZZFEED_content = getBUZZFEED.content

#parsing html contents to another variable using BeautifulSoup
Buzzfeed =soup(BUZZFEED_content, "html.parser")

#filtering through html script to extract specific parts of the website
top_news_container = Buzzfeed.findAll("div", {"class":"card card--article xs-relative xs-mb05 md-mb1 xs-border-left-none xs-border-right-none md-border-lighter js-feed-item"})

#creating csv file to store values
filename = "BuzzfeedNews.csv"
f = open(filename, "w")

#CSV column headers
headers = "Headline, Description, Author\n"
f.write(headers)

try:

    for news_item in top_news_container:

        Article = news_item.div.div.a.h2.text
        Description = news_item.div.div.a.p.text
        Author = news_item.span.text.strip()

#comment back in to print to console
        '''print("Article :" + Article)
        print("Description :" + Description)
        print("Author :" + Author)'''

        f.write(Article.replace(",", "-") + "," + Description.replace(",", "-") + Author.replace(",", "-") + "\n")
    f.close()


except AttributeError:
    print("Scrape finished")