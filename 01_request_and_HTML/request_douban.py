import requests

# Without the header, status_code will be invalid(>400)
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"}
url = "https://movie.douban.com/top250"

response = requests.get(url, headers = header)
print(response.status_code)
print(response.text)