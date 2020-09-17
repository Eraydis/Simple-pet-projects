import requests
import pprint
a = 1


url = [
    'https://worldofwarcraft.com/ru-ru/',
    'https://twitter.com/home',
    'https://aws.amazon.com/',
    'https://tutsplus.com/',
    'https://medium.com/',
    'http://lurkmore.to/Python',
    'http://code.vonc.fr/',
    ]

for s in url:
    response = requests.get(s)
    for i in range (600):
        print(a)
        pprint.pprint(response.status_code)
        a+=1