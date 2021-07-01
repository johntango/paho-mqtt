import requests
import json

broker = "192.168.1.42"
port = 8080
topic = "v1/devices/me/telemetry"
accessToken = "6ewdYyKrcOaMvq0CjXhr"
data = [
    {
        "ts": 1591123823000,
        "values": {
            "TEMPERATURES": 100,
            "DEW_POINT": 28,
            "VALUE_X": 0
        }
    },
    {
        "ts": 1591123883000,
        "values": {
            "TEMPERATURES": 150,
            "DEW_POINT": 26,
            "VALUE_X": 10
        }
    },
    {
        "ts": 1591123943000,
        "values": {
            "TEMPERATURES": 209,
            "DEW_POINT": 25,
            "VALUE_X": -10
        }
    }
]

data = json.dumps(data)

headers = {'Content-Type': 'application/json', }

# url_post = 'g'
url_post = f"http://{broker}:{port}/api/v1/{accessToken}/telemetry"
print(url_post)
response = requests.post(url_post, headers=headers, data=data)
print(response)
entityType = 'default'
headers = {"Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJ1c2VySWQiOiI5OWY3ZDEwMC05ZWJiLTExZWItOTNjMi0yMWMyZmExZGZlNzQiLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiOTk3MzEwYTAtOWViYi0xMWViLTkzYzItMjFjMmZhMWRmZTc0IiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNjE4NzQ5NDg3LCJleHAiOjE2MTg3NTg0ODd9.fFeV5p50HXWpgQqHdYdJOHJlssRTSTQLinRnzVbhK7HGw_NEUdC5NtKV_qy_Xpr4eLmDubzEEfvQf4_UdO7ReQ", "refreshToken": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlJFRlJFU0hfVE9LRU4iXSwidXNlcklkIjoiOTlmN2QxMDAtOWViYi0xMWViLTkzYzItMjFjMmZhMWRmZTc0IiwiaXNQdWJsaWMiOmZhbHNlLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImp0aSI6IjliYTY0ZTZkLTQxMDQtNDZhZi1hNDJkLTQwYmIzNmM5ZmRjOCIsImlhdCI6MTYxODc0OTQ4NywiZXhwIjoxNjE5MzU0Mjg3fQ.WxPnAIUGVTQr4YksUm-nR-_jYqlqPzDZ1Gukgqed9htr5TtTJHO7t33YUdwHusmPjBtA_vCnLJgNHFyZUKBRZg"}"}

url_get = f"http://{broker}:{port}/api/plugins/telemetry/DEVICE/{accessToken}/keys/timeseries"
response = requests.get(url_get, headers=headers)
print(response.json())

# use this curl to get JWT token
# curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"username":"tenant@thingsboard.org", "password":"tenant"}' 'http://192.168.1.42:8080/api/auth/login'
# jwt = {"token":"","refreshToken":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlJFRlJFU0hfVE9LRU4iXSwidXNlcklkIjoiOTlmN2QxMDAtOWViYi0xMWViLTkzYzItMjFjMmZhMWRmZTc0IiwiaXNQdWJsaWMiOmZhbHNlLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImp0aSI6IjliYTY0ZTZkLTQxMDQtNDZhZi1hNDJkLTQwYmIzNmM5ZmRjOCIsImlhdCI6MTYxODc0OTQ4NywiZXhwIjoxNjE5MzU0Mjg3fQ.WxPnAIUGVTQr4YksUm-nR-_jYqlqPzDZ1Gukgqed9htr5TtTJHO7t33YUdwHusmPjBtA_vCnLJgNHFyZUKBRZg"}
