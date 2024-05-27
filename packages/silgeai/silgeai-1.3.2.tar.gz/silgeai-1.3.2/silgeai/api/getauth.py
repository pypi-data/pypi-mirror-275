# -*- coding:utf-8 -*-
"""
@Author: 风吹落叶
@Contact: waitKey1@outlook.com
@Version: 1.0
@Date: 2024/5/27 6:19
@Describe: 
"""
import json
import requests
def getASRAIAuth(apikey,cagetory,uid='100002'):

    url = "http://154.41.229.92:8001/api/getasr_key"
    payload = json.dumps({
       "uid": uid,
       "apikey": apikey,
       "cagetory": cagetory
    })
    headers = {
       'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
       'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

#    print(response.text)
    try:
        json_response = response.json()
        json_response.update({'ret': 0})
        return json_response
    except:
        return {'ret':-1}

