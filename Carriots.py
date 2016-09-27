#-*-coding:utf8-*-
"""
    Carriots.py

    Created by Christian Escalante on 27 Sep 2016
"""

from urllib2 import urlopen, Request
from json import dumps, loads
import json


class Carriots (object):
    api_url = "http://api.carriots.com/"

    def __init__(self, api_key=None, client_type='json'):
        self.client_type = client_type
        self.api_key = api_key
        self.content_type = "application/vnd.carriots.api.v2+%s" % self.client_type
        self.headers = {'User-Agent': 'Raspberry-Carriots',
                        'Content-Type': self.content_type,
                        'Accept': self.content_type,
                        'Carriots.apikey': self.api_key}
        self.payload = None
        self.response = None

    def send_stream(self, device, data):
        payload = {"protocol": "v2", "device": device, "at": "now", "data":data}
        self.payload = dumps(payload)
        request = Request(self.api_url + "streams", self.payload, self.headers)
        self.response = urlopen(request)
        return self.response

    def get_device(self, device):
        self.payload = None
        request = Request(self.api_url + "devices/" + device, self.payload, self.headers)
        self.response = urlopen(request)
        return json.loads(self.response.read())

    def get_device_properties(self, device):
        self.payload = None
        request = Request(self.api_url + "devices/" + device, self.payload, self.headers)
        self.response = urlopen(request)
        return json.loads(self.response.read()).get("properties")