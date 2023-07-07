import requests

request = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
print(request.status_code)
data = request.json()
print(len(data))
for i in data["data"]:
    print(i)
