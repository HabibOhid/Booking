# For project mapping
class User:
    def __init__(self, name, country, passport, gender):
        self.name = name
        self.country = country
        self.passport = passport
        self.gender = gender

    def userInfo(self):
        print("User info " + self.name +
              self.country + self.passport + self.gender)
