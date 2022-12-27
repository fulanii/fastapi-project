




import requests as req


url = "http://localhost:8000/token"
header = {
  "Authorization": "Bearer alice"
}
body = {
  "username": "alice",
  "password": "secret2"
}

res = req.post(url, data=body)
print(res.text)



