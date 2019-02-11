import json
import requests
from datetime import datetime

def create_password():
    # with open("data1.json", 'r') as file:
    #     data = json.load(file)
    #     secik = set(data)
    #     print(secik)
    password = []
    wget = requests.get('https://pylove.org/exercise/1_19_1')
    data = wget.json()
    secik = set(data)
    for s in secik:
        if s.isalpha():
            password.append(s)
    print(' '.join(password))

if __name__ == '__main__':
    start = datetime.now()
    print('START: '+str(start))
    create_password()
    end = datetime.now()
    print('END: '+str(end))
    dif = end - start
    print('TIME: '+str(dif))