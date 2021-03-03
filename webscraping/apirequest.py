import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"\"metric\" or \"imperial\"","mode":"xml, html"}

headers = {
    'x-rapidapi-key': "28ffaf8ec4msh304d2d9f030e529p10a1b2jsncde1a9321a3d",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
read=response.text
read=read[5:]
import json
dict1={}
json.dumps([read])
js=json.loads(json.dumps([read]))
out_dictionary={}
for index,value in enumerate(js):
    out_dictionary[index]=value
