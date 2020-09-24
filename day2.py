print('------------------------------------------------------------')
# problem 6. FizzBuzz (Multiple of 3 is Fizz, Multiple of 5 is Buzz)
for i in range(1,101):
    if i % 15 == 0:
        print("Fizz Buzz!")
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
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

haveYen = int(input("plz input yen "))
exchange = YenToCurrency(haveYen)
print(str(haveYen) + 'yen is {} doll'.format(exchange.doll()))
print(str(haveYen) + 'yen is {} euro'.format(exchange.euro()))

print('------------------------------------------------------------')
# problem 9. euro to yen, doll to yen
