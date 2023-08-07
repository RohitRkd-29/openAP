
from collections import UserDict
import requests
import Key
import json

# Set the request parameters
url = 'https://deloitteitops.service-now.com/api/now/attachment/00031755eb71310020ee20b6a206fe3d/file'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"*/*"}
usr='intuser'
pwd='Ashish@123'
# Do the HTTP request
response = requests.get(url, auth=(usr, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response._content.decode()
#download_link = data["result"][0]["download_link"]
print(data)


