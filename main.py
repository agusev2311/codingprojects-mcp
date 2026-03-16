import get_cookies
import parser

base_url = "https://codingprojects.ru/"
cookies = get_cookies.get_cookies(base_url=base_url)
courses = parser.parse_courses(cookies=cookies, base_url=base_url)

print("Choose course to parse: ")
for i in range(len(courses)):
    print(f" {i + 1}. {courses[i]["name"]}")

course_number = int(input()) - 1

