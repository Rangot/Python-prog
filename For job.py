# по ссылке, словно отдаете книгу в руки
list = []
dic = {'puppy': 'hi puppy'}
s = set()

# по значению, словно отдаете копию
k = ()
a = 5
b = 6.6
d = 'Hello'

# вызов функции самой себя - рекурсия
def f(a):
    if a <= 0:
        return 0
    return a + f (a - 1)
    
print(f(5))
f(-1)

