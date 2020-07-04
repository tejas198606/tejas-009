import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Pclass':2,'Age':9,'Siblings':6,'Parents':2,'Fare':9})

print(r.json())

