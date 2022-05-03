import requests
url=("https://hub.dummyapis.com/delay?seconds=1")
res=requests.get(url)
print(res.content)
