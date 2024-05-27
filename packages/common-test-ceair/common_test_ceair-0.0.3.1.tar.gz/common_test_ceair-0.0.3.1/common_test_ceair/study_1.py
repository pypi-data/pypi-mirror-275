# -*- coding: utf-8 -*-
import requests


res = requests.get(url='https://www.boredapi.com/api/activity')

print(res.text)
