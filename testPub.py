import http.client
import mimetypes
conn = http.client.HTTPConnection("localhost", 8080)
payload = "{\"temperature\":43,\"humidity\":77}"
headers = {'Content-Type': 'application/json'}
conn.request("POST", "/api/v1/DHT11_DEMO_TOKEN/telemetry", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
