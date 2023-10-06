from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

with open("movies.txt", mode="w") as fp:
    for title in titles[::-1]:
        fp.write(f"{title}\n")