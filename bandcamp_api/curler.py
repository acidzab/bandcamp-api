import json
import urllib
from io import BytesIO
from urllib.parse import quote

import pycurl
from pycurl import Curl


def curl_api(url, headers):
    buffer = BytesIO()
    curler = Curl()
    curler.setopt(pycurl.URL, url)
    curler.setopt(pycurl.WRITEDATA, buffer)
    if headers:
        headers_list = []
        for header in headers.keys():
            headers_list.append(f'{header}: {headers[header]}')
        curler.setopt(pycurl.HTTPHEADER, headers_list)
    curler.perform()
    curler.close()

    return json.loads(buffer.getvalue().decode('utf-8'))
