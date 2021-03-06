import requests
from bs4 import BeautifulSoup

url = "https://www.sehir.edu.tr/tr/duyurular/2019_2020_akademik_yili_bahar_donemi_ders_programi"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
tb = soup.find('tbody')

courses = []

for tr in tb.find_all('tr'):
    for td in tr.find_all('td'):
        item = td.get_text()
        courses.append(item.replace("\r\n", ("")))


def makeNull(x):
    if x == "\xa0" or x == "-":
        x = None
    return x


courses = map(lambda x: makeNull(x), courses)
courses = list(courses)

codes = courses[0::6]
names = courses[1::6]
days = courses[2::6]
hours = courses[3::6]
rooms = courses[4::6]
instructors = courses[5::6]

print(codes)
print(names)
print(days)
print(hours)
print(rooms)
print(instructors)
