print('------------------------------------------------------------')
# problem 6. FizzBuzz (Multiple of 3 is Fizz, Multiple of 5 is Buzz)
for i in range(1,101):
    if i % 15 == 0:
        print('Fizz Buzz!')
    elif i % 3 == 0:
        print('Fizz!')
    elif i % 5 == 0:
        print('Buzz!')
    else:
        print(i)
print('------------------------------------------------------------')
# problem 7. how many z in n (Multiple of 3 is Fizz, Multiple of 5 is Buzz)
def count_z(n):
    print((n // 3 * 2) + n // 5 * 2)

count_z(100)
print('------------------------------------------------------------')
# problem 8. euro to yen, doll to yen
class YenToCurrency:
    def __init__(self,yen):
        self.yen = yen

    def doll(self):
        doll = self.yen / 109
        return(doll)

    def euro(self):
        euro = self.yen / 129
        return(euro)

haveYen = int(input('plz input yen '))
exchange = YenToCurrency(haveYen)
print(str(haveYen) + 'yen is {} doll'.format(exchange.doll()))
print(str(haveYen) + 'yen is {} euro'.format(exchange.euro()))

print('------------------------------------------------------------')
# problem 9. RPGgame class
class Character:
    def __init__(self, name, maxhp, attack_point, defence_point):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.attack_point = attack_point
        self.defence_point = defence_point

    def status(self):
        return '{}:helth {}/{}:attack_point {} defence_point {}' .format(self.name,self.hp,self.maxhp,self.attack_point,self.defence_point)

    def attack(self,enemy):
        cal_attack_point = self.attack_point - enemy.defence_point
        enemy.hp -= cal_attack_point
        print('attack of {} ! {} received {} damage !'.format(self.name,enemy.name,cal_attack_point))


koki = Character('KOKI',60,10,2)
slime = Character('Slime',15,5,1)

print(koki.status())
print(slime.status())

koki.attack(slime)
slime.attack(koki)

print(koki.status())
print(slime.status())

print('------------------------------------------------------------')
# problem 10. hashnumber
def j_hash(n):
    s = str(n)
    array = list(map(int, list(s)))
    a = sum(array)
    if n % a == 0:
        print('Hashnumber')
    else:
        print('Not hashnumber')

j_hash(int(input('plz input like number')))