class MyList(list):

    def __new__(cls, *args, **kwargs):
        print('Работает магический метод')
        return super().__new__(cls, *args, **kwargs)

    def __str__(self):
        print('Работает магический метод')
        return super.__str__(self)
    def __getitem__(self, item):
        print('Работает магический метод')
    def __setitem__(self, key, value):
        print('Работает магический метод')
    def __len__(self):
        print('Работает магический метод')
        return super().__len__()




lst = MyList(['Jone', 'Snow', 'Java'])
if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))
#
# Работает магический метод
# Работает магический метод
# Работает магический метод
# Работает магический метод
# ['Jone', 'Snow', 'Python']
# Работает магический метод
# 3