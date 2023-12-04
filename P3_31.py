import requests

url_games = "https://soccer365.ru/competitions/12/results/"
r = requests.get(url_games)
print(r.status_code)
print(r.headers["content-type"])
print(r.encoding)
print(r.text[:5000])
