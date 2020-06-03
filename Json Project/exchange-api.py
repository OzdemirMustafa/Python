import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="
satılan_doviz_tipi= input("Satılan Döviz Tipi\n")
alınan_doviz_tipi= input("Alınan Döviz Tipi\n")
miktar = float(input("Bozdurulan Miktar\n"))


result = requests.get(api_url+satılan_doviz_tipi)
result = json.loads(result.text)
carpim = miktar * result["rates"][alınan_doviz_tipi]

print(result["rates"])
print("1 {} = {} {} 'e karşılık gelmektedir.".format(satılan_doviz_tipi,result["rates"][alınan_doviz_tipi],alınan_doviz_tipi))
print("{} {} {} {}'e karşılık geliyor! Alışverişler !!!".format(miktar,satılan_doviz_tipi,carpim,alınan_doviz_tipi))
