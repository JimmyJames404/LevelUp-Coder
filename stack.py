import requests
from bs4 import BeautifulSoup
from collections import Counter
import math
from lxml import etree
 
def main(link):
    github_html = requests.get(f'{link}').text
    soup = BeautifulSoup(github_html, "html.parser")
    stats = []
    for span in soup.find_all('div',class_="fs-body3 fc-dark"):
            stats.append(span.string)
    reputacion = stats[0]
    reached = stats[1]
    answers = stats[2]
    questions = stats[3]

    date = []
    data= ''
    for data in soup.find_all("span"): 
        date.append(data.string)
    date = date[16]

    result = {
        'reputacion' : reputacion,
        'reached' : reached,
        'answers' : answers,
        'questions' : questions,
        'date' : date   
    }
    print(result)
    return result
 
if __name__ == "__main__":
    user = "https://stackoverflow.com/users/14452043/jimmy-j"
    main(user)