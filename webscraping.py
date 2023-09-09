import requests
from bs4 import BeautifulSoup
from bs4.element import Comment


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
url = "https://papersowl.com/examples/my-family-trip-to-miami/"
def scrape(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.content,"html.parser")

    content = soup.findAll(text = True)

    res = soup.title

    visible_content = filter(tag_visible,content)
    return u" ".join(t.strip() for t in visible_content)

#print(scrape(url))