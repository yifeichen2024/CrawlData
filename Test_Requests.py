import requests 

head =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"} # Add header can fake code request to a browser request
response = requests.get("http://books.toscrape.com/", headers = head)

if response.ok: 
    print(response.text)
else:
    print("Fail to request")
# print(response.ok) # Return the request success status.
# print(response)
# print(response.status_code) # Return with the status code. >=200 and < 400 is ok to get content.
