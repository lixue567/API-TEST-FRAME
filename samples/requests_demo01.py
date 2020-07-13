import requests
response = requests.get('http://www.hnxmxit.com/')
print(response.apparent_encoding)
response.encoding = response.apparent_encoding
print(response.headers)
