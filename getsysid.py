#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://deloitteitops.service-now.com/api/now/attachment?sysparm_query=KnowledgeReport.csv&sysparm_limit=1'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'intuser'
pwd = 'Ashish@123'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
sys_id = data["result"][0]["sys_id"]
print(sys_id)


url2 = 'https://deloitteitops.service-now.com/api/now/attachment/'+sys_id+'/file'
print(url2)
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
data2 = response._content.decode()
#download_link = data["result"][0]["download_link"]
print(data2)

