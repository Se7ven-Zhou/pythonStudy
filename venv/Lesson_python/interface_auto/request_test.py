# utf-8

import requests

url = "https://account.xiaomi.com/pass/serviceLoginAuth2?_dc=1533019185955"
datas = {"hash":"9ACD8B4959B54EE3141DDED2C056B7AB","user":"13752852018","_sign":"RGfMpi9Bf4f63t6MqC02xCDiBmc=","sid":"mi_eshop"}
# cookie = xxx

result = requests.request("POST",url,data = datas)

print(result.headers)
