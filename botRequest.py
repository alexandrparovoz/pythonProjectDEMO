# делаю запрос на намберсфпи для числа 43

import requests
api_address =  'http://numbersapi.com/43'
res = requests.get(api_address)
if res.status_code == 200:
    print(res.text)
else:
    print(res.status_code)