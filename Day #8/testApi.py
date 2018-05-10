import requests
import json
from contextManager import Manager

config = {'host': '127.0.0.1',
          'user': 'root',
          'password': 'password',
          'database': 'Contact', }

def main():
    with Manager(config) as cursor:
        _SQL = "INSERT INTO users(name,password,email,phone) VALUES(%s, %s, %s, %s)"
        for i in range(0,100):
            res = requests.get('https://randomuser.me/api/')
            raw = json.loads(res.content)    
            data = raw['results'][0]
            name = data['name']['first']
            email = data['email']
            password = data['login']['password']
            phone = data['phone']
            cursor.execute(_SQL,(name,password,email,phone))
            print("User succefully added")

if __name__ == "__main__":
    main()