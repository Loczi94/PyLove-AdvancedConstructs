from collections import Counter
import requests

def find_password():
    password = ''
    wget = requests.get('https://pylove.org/exercise/1_19_2')
    data = wget.text
    c = Counter(data)
    password_list = c.most_common(6)
    for p in password_list:
        password += p[0]
    print(password)


if __name__ == '__main__':
    find_password()