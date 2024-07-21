import requests
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"}
url = "https://movie.douban.com/top250"
for start_num in range(0, 250, 25):
    contend = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=header).text
    soup_douban_top250 = BeautifulSoup(contend, "html.parser")

    titles = soup_douban_top250.find_all("span", attrs={"class" : "title"})
    for title in titles:
        title_name = title.string
        if "/" not in title_name:
            print(title_name)



