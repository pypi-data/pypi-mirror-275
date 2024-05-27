# -*- coding: utf-8 -*-
import requests


res = requests.post(url='http://paassit07.ceair.com/mu/authentication/service/rest-auth/loginForMobile', json={
    "mobileNo": "15514525653",
    "accountType": "MOBILE",
    "salesChannel": "7301"
})

print(res.text)
