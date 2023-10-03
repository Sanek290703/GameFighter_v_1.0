import random
import time

class Printer():
    def __init__(self):
        self.admin = '''
    Здравствуйте, Александр! 
Не ожидали вас так скоро увидеть!

Режим АДМИНА включен:
'''
        self.start = '''Добро пожаловать в МИР МЕЧА И ЩИТА
Как мне вас называть?
    НИК:'''
        self.hi = '''
Приветствую тебя, {} 
Теперь давай выберем тебе подходящий класс
(Выбор не большой, но важный)

Но, не смотря на классы, все удары будут варироваться
(точное чило дамага нельзя знать на 100%)
P.s. У врагов тоже!'''
        self.clas = '''Классы:
    1. Мечник:
        У вас есть огромный шанс крита,
        но так же можете ударить слабо...
        (Класс для везунчиков)
        Ваш урон варируется от 10 до 70
    2. Дефендер:
        У вас есть защита 15,
        но зато щит мешает драться...
        (Класс для стабильных игроков)
        Ваш урон варируется от 15 до 30

Чтобы выбрать класс напиши цифру класса
    Ваш выбор: '''
        self.menu = '''  \nВы находитесь в МЕНЮ:    
        1 - Магазин
        2 - Атрибуты/Рюкзак
        3 - БОЙ
    Куда идем? '''
        self.bag = '''        Coins {}
        Врагов побеждено {}'''
        self.battle = '''    \nВы в БОЮ!      
        1 - Удар
        2 - Использовать хилл (Это +60 ХР)
    Что делаем? '''
        self.shop = '''\nМАГАЗИН (у тебя всего {} в кошеле)                                                      
        1 - Купить хилку (4 coins)
        2 - Прокачка своего класса (8 coins)
        3 - Назад
    Что делаем? '''
        self.atribut = '''        Имя {}
        ХР {}
        Урон от {} до {}
        Защита {}
        Хилки {}'''

        self.win = 'Поздравляю, {}, был силен, но вы сильнее!'
        self.loose = 'Вы погибли от руки {}\n      GAME OVER'
        self.lut = '''Вы залутали с трупа {} coins
Ваши ХР немного восстановились, теперь у вас {} ХР
        1 - Фармим
        2 - На БОССА
    Что делаем? '''
        self.miss = '\nНу ты и косой! По кнопке попасть сложно?\n'
        self.win_game = '''
    Мои поздравления, {}!
    Вы только что победили ОЧЕНЬ ЗЛОГО И СТРАШНОГО БОССА
    Спасибо, что играли в мою игру!
    До новых встреч на просторах двоичного кода, путник'''


printer = Printer()


class Creature(): #TODO переименовать, так как очень абстрактное понятие и используется зачастую в фреймворках
    def __init__(self):
        self.name = ''
        self.hp = 150
        self.damage = 5
        self.l_range = 4
        self.r_range = 6
        self.resist = 0
        self.hill = 0
        self.coins = 15
        self.prokachka = 9

    def hit(self):  # Удар
        return random.randint(int(self.damage * self.l_range), self.damage * self.r_range)

    def is_died(self):
        if self.hp <= 0:
            self.hp = 0
            print()
            print(self.name, 'погибает в бою...\n')
            return False
        else:
            return True


class Person(Creature):
    pass


class Animy(Creature):
    pass


def money(a, n):
    if a.coins >= n:
        a.coins = a.coins - n
        return True
    else:
        print('\nДенег не хватает, вали отсюда, раз считать не умеешь!')
        return False


def shop(a):
    while True:  # SHOP
        print(printer.shop.format(a.coins), end='')
        n = input()
        if n == '1':  # 12 SHOP_BUY
            if money(a, 4):
                a.hill += 1
                print('\n+ Хилка')
            else:
                break
        elif n == '2':
            if a.resist == 0:
                if money(a, 8):
                    if a.prokachka > 0:
                        a.l_range += 1.2
                        a.prokachka -= 1
                        print('\nРазброс уменьшился на 6')
                    else:
                        a.coins += 8
                        print('\nВы достигли максимального уровня прокачки!')
                else:
                    break
            else:
                if money(a, 8):
                    if a.prokachka > 0:
                        a.resist += 3
                        a.prokachka -= 1
                        print('\nЗащита увеличилачь на 3')
                    else:
                        a.coins += 8
                        print('\nВы достигли максимального уровня прокачки!')
                else:
                    break

        elif n == '3':
            break
        else:
            print(printer.miss)


def battle(a, b):
    while a.is_died() and b.is_died():
        while True:
            print(printer.battle, end='')
            d = input()
            print()
            if d == '1':
                a_hit = a.hit()
                if b.hp <= 70 and b.hill > 0:
                    b.hill -= 1
                    b.hp += 70
                    print(f"{b.name} отхилил 70 XP, его ХР {b.hp} \n")
                    time.sleep(1)
                    b.hp -= a_hit - b.resist if a_hit > b.resist else 0
                    print(a.name, "снимает", a_hit - b.resist if a_hit > b.resist else 0, '''жизней! ''', '\n')
                else:
                    b_hit = b.hit()
                    a.hp -= b_hit - a.resist if b_hit > a.resist else 0
                    b.hp -= a_hit - b.resist if a_hit > b.resist else 0
                    print(a.name, "снимает", a_hit - b.resist if a_hit > b.resist else 0, '''жизней! ''')
                    print(b.name, "снимает", b_hit - a.resist if b_hit > a.resist else 0, '''жизней! ''', end='\n\n')
                print(a.name, ' =', a.hp if a.hp > 0 else 0, 'XP')
                print(b.name, ' =', b.hp if b.hp > 0 else 0, 'XP')
                time.sleep(1)
                break
            if d == '2':
                if a.hill > 0:
                    a.hill -= 1
                    a.hp = a.hp + 60 if a.hp + 60 < 150 else 150
                    print("Ваши ХР", a.hp)
                    print()
                    if b.hp <= 70 and b.hill > 0:
                        b.hill -= 1
                        b.hp += 100
                        print(f"{b.name} отхилил 100 XP, его ХР {b.hp} \n")
                    else:
                        time.sleep(1)
                        b_hit = b.hit()
                        a.hp -= b_hit - a.resist if b_hit > a.resist else 0
                        print(b.name, "снимает", b_hit - a.resist if b_hit > a.resist else 0, '''жизней! ''',
                              end='\n\n')
                    print(a.name, ' =', a.hp if a.hp > 0 else 0, 'XP')
                    print(b.name, ' =', b.hp if b.hp > 0 else 0, 'XP')
                    time.sleep(1)
                    break
                else:
                    print('\nХилок НЕТ!')
            else:
                print(printer.miss)
    if a.hp == 0:
        return -1, printer.loose.format(b.name)
    return 0, printer.win.format(b.name)


print(printer.start, end=' ')
a = Person()
a.name = input()
print(printer.hi.format(a.name), end='\n\n')
time.sleep(3)

count = 0

while True:
    print(printer.clas, end='')
    n = input()
    if n == '1':
        a.damage, a.l_range, a.r_range, a.hill = 5, 2, 14, 4
        break
    if n == '2':
        a.damage, a.l_range, a.r_range, a.resist, a.hill = 5, 3, 6, 15, 3
        break
    elif n == 'Nal54212_29':
        # clear = lambda: system('cls')
        # clear()
        a.name, a.hp, a.damage, a.l_range, a.r_range, a.resist, a.hill, a.coins = 'Санёк_29', 1000, 1000, 1, 20, 100, 29, 1000
        print(printer.admin)
        print(printer.atribut.format(a.name, a.hp, int(a.damage * a.l_range), a.damage * a.r_range, a.resist, a.hill))
        count = 290
        print(printer.bag.format(a.coins, count))
        time.sleep(5)
        break
    else:
        print(printer.miss)

print('''
Теперь все просто - варианты выбираешь клавишами:
1, 2 или 3:''')
global BOSS
BOSS = 0
while BOSS != -1:
    while BOSS == 0:
        print(printer.menu, end='')
        print(BOSS)
        n = input()
        if n == '1':
            shop(a)
        elif n == '2':  # BAGAGE
            print('\nАтрибуты/Рюкзак')
            print(
                printer.atribut.format(a.name, a.hp, int(a.damage * a.l_range), a.damage * a.r_range, a.resist, a.hill))
            print(printer.bag.format(a.coins, count))
            time.sleep(5)
            break
        elif n != '3':
            print(printer.miss)
        elif n == '3':
            count += 1  # Creation
            b = Animy()
            b.name = "Воин_" + str(count)

            if a.resist == 0:
                b.damage = random.randint(5, 8)
                if b.damage < 7:
                    b.hp, b.hill, b.resist = random.randint(90, 120), random.randint(1, 2), random.choice(
                        [0, 0, 0, 10, 10, 15])
                else:
                    b.hp, b.hill, b.resist = random.randint(80, 100), random.randint(0, 1), random.choice(
                        [0, 0, 0, 0, 15])
            else:
                b.damage = random.randint(6, 10)
                if b.damage < 9:
                    b.hp, b.hill, b.resist = random.randint(70, 100), random.randint(0, 2), random.choice(
                        [0, 0, 0, 0, 10, 5])
                else:
                    b.hp, b.hill = random.randint(60, 100), random.randint(0, 1)

            print()
            print(printer.atribut.format(b.name, b.hp, b.damage * b.l_range, b.damage * b.r_range, b.resist, b.hill))

            BOSS, p = battle(a, b)
            print(p)

            if BOSS == 0:
                coins = random.randint(4, 11)
                a.coins += coins
                a.hp = a.hp + 100 if a.hp + 100 <= 150 else 150
                print(printer.lut.format(coins, a.hp), end='')
                while True:
                    n = input()
                    if n == '1':
                        break
                    elif n == '2':
                        BOSS = 1
                        break
                    else:
                        print(printer.miss)

    if BOSS == 1:
        c = Animy()
        c.name = "ОЧЕНЬ ЗЛОЙ И СТРАШНЫЙ БОСС"
        if a.resist == 0:
            c.resist, c.l_range, c.r_range, c.hill = 30, 4, 11, 5
        else:
            c.resist, c.l_range, c.r_range, c.hill = 10, 12, 18, 2
        print()
        print(printer.atribut.format(c.name, c.hp, c.damage * c.l_range, c.damage * c.r_range, c.resist, c.hill))
        while BOSS == 1:
            print(printer.menu)
            print("        4 - Если думаешь, что слабоват (Продолжить фарм) ")
            n = input()
            if n == '1':
                shop(a)
            elif n == '2':  # BAGAGE
                print('\nАтрибуты/Рюкзак')
                print(printer.atribut.format(a.name, a.hp, int(a.damage * a.l_range), a.damage * a.r_range, a.resist,
                                             a.hill))
                print(printer.bag.format(a.coins, count))
                time.sleep(5)
                break
            elif n == "4":
                BOSS = 0
                break
            elif n != '3':
                print(printer.miss)
            elif n == '3':
                BOSS, p = battle(a, c)
                print(p)
                if BOSS == 0:
                    print(printer.win_game.format(a.name))
        BOSS = -1
