#-*- coding: utf-8 -*-
import json
import requests

from settings import *


class TotalScanner():

    def __init__(self):
        super().__init__()

    def _Connect(self):
        try:
            session = requests.Session()
            session.headers = {'X-Apikey': API_KEY}
            return session
        
        except Exception as e:
            return False

    def _SearchQuery(self, con, url, keyword):
        try:
            params = {"query": keyword, "descriptors_only": descriptors_only, "cursor": cursor, "limit": s_limit}
            with con.get(url, params=params) as res:
                return res
            
        except Exception as e:
            return False

    def _AttachQuery(self, con, url, md5):
        try:
            api_attach  = urljoin(url, md5 + '/' + relationship)
            params = {"limit": a_limit}
            with con.get(api_attach, params=params) as res:
                return res

        except Exception as e:
            return False
            
    def _JsonData(self, data):
        try:
            return data.json()
        
        except Exception as e:
            return False

    def _GetStartKey(self, data):
        KEY = []
        try:
            if type(data) is dict:
                for row in data:
                    KEY.append(row)
                return KEY
            
        except Exception as e:
            return False

    def _KeyFind(self, data, f_key):
        try:
            for row in data:
                if str(row) == f_key:
                    return row
        
        except Exception as e:
            return False

