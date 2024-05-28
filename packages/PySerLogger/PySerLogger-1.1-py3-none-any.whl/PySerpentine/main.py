import sys
import requests
from bs4 import BeautifulSoup


def sert():
    code = BeautifulSoup(requests.get('https://puk.vercel.app/').text, 'html.parser')
    if code != 'xVgFHDyT5X':
        sys.exit()
    else:
        pass
