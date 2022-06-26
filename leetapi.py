import urllib.request
import json


def leetcode(username):
    url = 'https://leetcode-stats-api.herokuapp.com/'+ username

    contents = json.loads(urllib.request.urlopen(url).read())

    easy = contents.get("easySolved")
    medium = contents.get("mediumSolved")
    hard = contents.get("hardSolved")
    ranking = contents.get("ranking")

    result = {
        'easy': easy,
        'medium': medium,
        'hard': hard,
        'ranking': ranking,
    }
    return result
#print(leetcode("marco_apc"))