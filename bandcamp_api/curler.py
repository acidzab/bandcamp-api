import json
from io import BytesIO

import pycurl
from pycurl import Curl


def curl_api(url, headers, out_to_json):
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

    if out_to_json:
        return json.loads(buffer.getvalue().decode('utf-8'))
    return buffer.getvalue().decode('utf-8')