# problem 1. sum(1~50)
print('------------------------------------------------------------')
s = 0
for i in range(1,51):
    # print(i) >>number 1~50
    s += i
print(s)

s = sum(range(1,51))  # another answer
print(s)
print('------------------------------------------------------------')
# problem 2. Prime numbers less than 1000
for i in range(2,1001):
    for n in range(2,i):
        if i%n == 0:
            break
    else:             # 段落に気を付ける
        print(i)
print('------------------------------------------------------------')
# problem 3. Display the 10th Fibonacci sequence 

print('------------------------------------------------------------')
# problem 4. Display the least common multiple/greatest common divisor of two natural numbers
print('------------------------------------------------------------')
# problem 5. Multiples of 3 less than 100
print('------------------------------------------------------------')