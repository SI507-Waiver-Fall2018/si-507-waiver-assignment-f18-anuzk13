# these should be the only imports you need

import requests
import bs4

# write your code here
# usage should be python3 part3.py
url = "https://www.michigandaily.com/"
result = requests.get(url)
if (result.status_code == 200):
    content = result.content
    soup = bs4.BeautifulSoup(content, 'html.parser')
    articles = soup.find("div", {"class": "view-most-read"}).findAll("a")
    for article in articles:
        sub_result = requests.get(url + article['href'])
        if (sub_result.status_code == 200):
            sub_content = sub_result.content
            sub_soup = bs4.BeautifulSoup(sub_content, 'html.parser')
            a_div = sub_soup.find("div", {"class": "byline"})
            author = 'Not Listed' if a_div is None else a_div.find("a").string
            print(article.string)
            print(' by {}'.format(author))
