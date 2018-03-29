import requests
import json
import time
import sys
from collections import OrderedDict
import xml.etree.ElementTree as ET

base_url = 'http://csearch.naver.com/dcontent/spellchecker.nhn'
_requestAgent = requests.Session()


def checkSpace(text):
    if len(text) > 500:
        return -1

    payload = {
        '_callback': 'window.__jindo2_callback._spellingCheck_0',
        'q': text
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }

    response = _requestAgent.get(base_url, params=payload, headers=headers)
    response = response.text[42:-2]

    data = json.loads(response)
    str_resultHtmlData = data['message']['result']['html']

    str_resultData = str(str_resultHtmlData).replace('<span class=\'re_green\'>', '') \
        .replace('<span class=\'re_red\'>', '') \
        .replace('<span class=\'re_purple\'>', '') \
        .replace('</span>', '')

    return str_resultData
