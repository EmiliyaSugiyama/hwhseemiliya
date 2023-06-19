import requests
from bs4 import BeautifulSoup

# Загрузка страницы с эмодзи
url = "https://emojipedia.org/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Поиск разделов "nature", "music" и "science"
nature_section = soup.find("h2", text="Nature").find_next("ul")
music_section = soup.find("h2", text="Music").find_next("ul")
science_section = soup.find("h2", text="Science").find_next("ul")

# Подсчет количества emoji в каждом разделе
nature_count = len(nature_section.find_all("li"))
music_count = len(music_section.find_all("li"))
science_count = len(science_section.find_all("li"))

# Вывод результатов
print("Количество emoji в разделе Nature:", nature_count)
print("Количество emoji в разделе Music:", music_count)
print("Количество emoji в разделе Science:", science_count)
