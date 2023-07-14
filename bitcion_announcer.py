import requests
import json
import pyttsx3

endpoint = 'https://api.coindesk.com/v1/bpi/currentprice.json'
res = requests.get(endpoint)
data = json.loads(res.text)
bitcoin_price = (data['bpi']['USD']['rate']).replace(',','')
bitcoin_price = int(float(bitcoin_price))
response =f' Bitcoin price is {bitcoin_price}'
engine = pyttsx3.init()
engine.say(response)
engine.runAndWait()

