 class Car:
     name = 'MERS'
     def sayname(self):
         print(self.name)













class SuperHero:
    people = 'people'
def __init__(self, name, nickname, superpower, health_points, catchprase):
    self.name = name
    self.nickname = nickname
    self.superpower = superpower
    self.health_points = health_points
    self.catchprase = catchprase

def sayname(self):
    return self.name

def health_points_2(self):
    return self.health_points * 2


def __str__(self):
    return f'{self.nickname},{self.superpower},{self.health_points}'


def __len__(self):
    return len(self.catchprase)


people1 = SuperHero('Peter Parker', 'pookieman', 'climbing', 99, 'hiuhi')
people2 = SuperHero('elli', 'mamkakuhni', 'superbaking', 999, 'bakibak')
print(people1.name, people1.nickname, people1.superpower, people1.health_points * 2, people1.catchprase, len(people1))
print(people2.name, people2.nickname, people2.superpower, people2.health_points * 2, people2.catchprase, len(people2))
print(people1.sayname(), people1.health_points_2(), people1)