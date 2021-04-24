import json
import os


class RepositorioProfessionalProfile:
    def __init__(self):
        self.profiles = {}
        self.load()

    def save(self, profiles):
        self.profiles[profiles["email"]] = profiles

    def findUser(self, email):
        return self.profiles[email]

    def find(self, field, search):
        user_search = []
        for k, user in self.profiles.items():
            if user[field] == search:
                user_search.append(user)
            elif type(user[field]) is list:        
                for user_filde in user[field]:
                    if user_filde == search:
                        user_search.append(user)
        return user_search

    def find_all(self):
        # return self.profiles
        user_search = []
        for k, user in self.profiles.items():
            user_search.append(user)
        return user_search

    def load(self):
        profiles_data = {}
        if os.path.exists('data.json'):
            with open('data.json') as f:
                profiles_data = json.load(f)
        self.profiles = profiles_data


user = RepositorioProfessionalProfile()
A = {
    "email": "@gmail.com",
    "nome": "fabricio",
    "sobrenome": "souza",
    "residencia": "Ananideua",
    "formacao academica": [
            "ciencia da computacao"
    ],
    "habilidade": [
        "programação web"
    ],
    "experiencia": [
        "projeto pessoais em django"
    ]
}
