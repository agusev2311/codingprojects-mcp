import requests
from bs4 import BeautifulSoup

def parse_courses(cookies, base_url="https://codingprojects.ru/"):
    print("Parsing courses...")
    print(" > Requesting courses...")
    req = requests.get(base_url + "insider/courses", cookies=cookies)
    print(" > Parsing courses...")
    soup = BeautifulSoup(req.text, 'html.parser')

    courses = []

    for h5 in soup.find_all("h5"):
        if "courses" in h5.decode():
            courses.append({"href": h5.a.attrs["href"], "name": h5.a.get_text()})
    
    print(" v Successfully parsed")
    return courses
