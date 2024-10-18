# # from calendar import day_name
# # from functools import cache
# # from idlelib.zoomheight import set_window_geometry
# # from operator import truediv
# # from smtpd import usage
#
#
# class SuperHero:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         self.fly = False  # fly по умолчанию False
#
#     def multiply_hp(self):
#         # Метод умножает хп на 2 (будем переопределять в наследуемых классах)
#         self.hp = self.hp ** 2
#         self.fly = True
#
#     def true_phrase(self):
#         # Новый метод, выводит фразу True in the True_phrase
#         print("True in the True_phrase")
#
#
#
# class AirHero(SuperHero):
#     def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
#         super().__init__(name, nickname, superpower, health_points, catchphrase)
#         self.damage = damage
#         self.fly = False
#
#
# def health_points_2(self):
#     self.fly = True
#     return self.health_points ** 2
#
#
# def true_phrase(self):
#     return "True in the True_phrase"
#
#
# class EarthHero(SuperHero):
#     def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
#         super().__init__(name, nickname, superpower, health_points, catchphrase)
#         self.damage = damage
#         self.fly = False
#
#
#     def health_points_2(self):
#         self.fly = True
#         return self.health_points ** 2
#
#
# def true_phrase(self):
#     return "True in the True_phrase"
#
#
# class Villain(AirHero):
#     people = ('monster')
#     def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
#         super().__init__(name, nickname, superpower, health_points, catchphrase)
#         self.damage = damage
#         self.fly = False
#
#
#     def gen_x(self):
#         pass
#
#     def crit(self):
#         return self. damage ** 2
#
#
# air_hero = AirHero( name= 'Airy', nickname= 'WindMaster', superpower= 'flight', health_points= 100, catchphrase= 'Sky high', damage=50)
# earth_hero = EarthHero( name= 'Rocky', nickname= 'EarthShaker', superpower= 'Earth Manipulation', health_points= 120, catchphrase= 'Solid as a rock!', damage= 40)
#
#
#
# print(air_hero.sayname())
# print(air_hero.health_points_2())
# print(air_hero.true_phrase())
# print(air_hero.fly)
#
# print(earth_hero.sayname())
# print(earth_hero.health_points_2())
# print(earth_hero.true_phrase())
# print(earth_hero.fly())
#
# villain = Villain( name= 'Doom', nickname= 'DarkLord', superpower= 'Destruction', health_points= 150, catchphrase= 'Fear the shadows', damage= 60)
# print(villain.crit())
#
# -------------------------------

class SuperHero:
    def __init__(self, name, health_points, damage, superpower=None, nickname=None, catchphrase=None):
        self.name = name
        self.health_points = health_points
        self.damage = damage
        self.superpower = superpower
        self.nickname = nickname
        self.catchphrase = catchphrase
        self.fly = False  # fly по умолчанию False

    def multiply_hp(self):
        # Умножает хп на 2
        self.health_points *= 2
        self.fly = True

    def true_phrase(self):
        # Новый метод, выводит фразу
        print("True in the True_phrase")

    def __str__(self):
        return f"{self.name} (HP: {self.health_points}, Damage: {self.damage})"


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, health_points, damage, superpower, nickname, catchphrase)
        self.fly = True  # Воздушный герой всегда может летать

    def health_points_2(self):
        # Удваивает хп
        self.health_points *= 2
        return self.health_points


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, health_points, damage, superpower, nickname, catchphrase)
        self.fly = False  # Земной герой не может летать

    def health_points_2(self):
        # Удваивает хп
        self.health_points *= 2
        return self.health_points


class Villain(AirHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.fly = False  # Злодей не может летать

    def crit(self):
        # Критический урон - квадрат урона
        return self.damage ** 2


air_hero = AirHero(name='Airy', nickname='WindMaster', superpower='flight', health_points=100, catchphrase='Sky high', damage=50)
earth_hero = EarthHero(name='Rocky', nickname='EarthShaker', superpower='Earth Manipulation', health_points=120, catchphrase='Solid as a rock!', damage=40)

# Выводим информацию о героях:
print(air_hero)  # Пример использования метода __str__()
print(air_hero.health_points_2())
print(air_hero.true_phrase())
print("Fly ability:", air_hero.fly)

print(earth_hero)
print(earth_hero.health_points_2())
print(earth_hero.true_phrase())
print("Fly ability:", earth_hero.fly)

villain = Villain(name='Doom', nickname='DarkLord', superpower='Destruction', health_points=150, catchphrase='Fear the shadows', damage=60)
print("Villain critical damage:", villain.crit())
