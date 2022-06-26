from pygments import highlight
import requests
from bs4 import BeautifulSoup
from collections import Counter
import math
 
def github(username):
    if('https://'in username):
        username = username.split('/')[3]
    else:
        pass
    github_html = requests.get(f'https://github.com/{username}').text
    soup = BeautifulSoup(github_html, "html.parser")
    avatar_block = soup.find_all('img',class_='avatar')
    img_url = avatar_block[4].get('src')
    repos = soup.find('span',class_="Counter").text
    contributions = soup.find('h2',class_="f4 text-normal mb-2").text
    numeric_filter = filter(str.isdigit, contributions)
    contributions = "".join(numeric_filter)
    languages = []
    pages = math.ceil(int(repos)/30)
    
    onpage = 1
    for page in range(0,pages):
        github_html = requests.get(f'https://github.com/{username}?page={onpage}&tab=repositories').text
        soup = BeautifulSoup(github_html, "html.parser")
        for span in soup.find_all('span',itemprop="programmingLanguage"):
            languages.append(span.string)
        onpage += 1
    uniq = Counter(languages)
    languages = ", ".join(uniq.keys())
    
    highlights =([img['alt'] for img in soup.find_all('img', alt=True)])
    s = Counter(highlights)
    highlights = " ".join(s.keys())

    result = {
        'imgUrl' : img_url,
        'numRepos' : repos,
        'contributions' : contributions,
        'languages' : languages,
        'highlights' : highlights
    }
    #print(result)
    return result
 
if __name__ == "__main__":
    user = "dmalan"
    github(user)