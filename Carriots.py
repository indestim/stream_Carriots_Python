#-*-coding:utf8-*-
"""
    Carriots.py

    Created by Christian Escalante on 05 Oct 2016
"""

from urllib2 import urlopen, Request
from json import dumps, loads
import json


class Carriots (object):
    api_url = "http://api.carriots.com/"

    def __init__(self, account, api_key, client_type='json'):
        self.client_type = client_type
        self.api_key = api_key
        self.account = account
        self.content_type = "application/vnd.carriots.api.v2+%s" % self.client_type
        self.headers = {'User-Agent': 'Raspberry-Carriots',
                        'Content-Type': self.content_type,
                        'Accept': self.content_type,
                        'Carriots.apikey': self.api_key}
        self.payload = None
        self.response = None

    def set_device(self, device):
    	self.device = device + "@" + self.account + "." + self.account

    def send_stream(self, data):
        payload = {"protocol": "v2", "device": self.device, "at": "now", "data":data}
        self.payload = dumps(payload)
        request = Request(self.api_url + "streams", self.payload, self.headers)
        self.response = urlopen(request)
        return self.response

    def get_value_property(self, key_property):
        self.payload = None
        request = Request(self.api_url + "devices/" + self.device, self.payload, self.headers)
        self.response = urlopen(request)
        return json.loads(self.response.read()).get("properties").get(key_property)
