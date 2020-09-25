# problem 11. word sort
def sort_text(text):
    text = open(text).read().split()
    text.sort()
    print(text)

sort_text('number.txt')
print('------------------------------------------------------------')
# problem 12. how many 'a' in text
print(open('number.txt').read().count('a'))
print('------------------------------------------------------------')
