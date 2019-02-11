import requests
from collections import defaultdict
from datetime import datetime

def find_password():
    wget = requests.get('https://pylove.org/exercise/1_19_2')
    data = wget.text
    defdict = defaultdict(int)
    for let in data:
        defdict[let] += 1
    password = ''
    for _ in range(6):
        a_max = 0
        a_let = ''
        for key, value in defdict.items():
            if value > a_max:
                a_max = value
                a_let = key
        del defdict[a_let]
        password += a_let
    print(password)


if __name__ == '__main__':
    start = datetime.now()
    print('START: '+str(start))
    find_password()
    end = datetime.now()
    print('END: '+str(end))
    dif = end - start
    print('TIME: '+str(dif))