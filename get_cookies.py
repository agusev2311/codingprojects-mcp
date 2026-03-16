import requests
from bs4 import BeautifulSoup
import os
import pickle

def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)

def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def get_cookies():
    if not os.path.isfile("cookies.txt"):  
        base_url = "https://codingprojects.ru/"

        print("Trying to parse login page...")

        req = requests.get(base_url + "login")

        if req.status_code != 200:
            print(f" x Status code: {req.status_code} != 200")
            print("Exiting program...")
            exit(1)

        soup = BeautifulSoup(req.text, 'html.parser')

        token = soup.find_all("input")[0].get("value")

        cookies = req.cookies

        if token:
            print(f" v Success! Your token is {token} (useless info lol)")
        else:
            print(" x token != true")
            print("Exiting program...")
            exit(1)

        print("Let's login!")
        print("Enter your login: ")
        login = input()
        print("Now enter your password: ")
        password = input()

        print(" > Sending login request...")

        params = {
            "_token": token,
            "email": login,
            "password": password,
            "remember": "on"
        }

        req = requests.post(base_url + "login", params=params, cookies=cookies)

        if "These credentials do not match our records." in req.text:
            print(" x Invalid credentials")
            print("Exiting program...")
            exit(1)
        elif req.status_code:
            print(" v Success! Now you are logged in.")
        else:
            print(" x Unknown error")
            print("Exiting program...")
            exit(1)

        cookies = req.cookies
        save_cookies(cookies, "cookies.txt")
        print(" v Cookies saved")
    else:
        cookies = load_cookies("cookies.txt")
        print(" v Cookies loaded")
    return cookies