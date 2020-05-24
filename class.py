class Student(object):

    def __init__(self, value):
        self._value = value



    def __getattr__(self, item):
        if item == 'path':
            print('Path is {}'.format(item))
        raise AttributeError('No Such parameter')



GY = Student(1)

print(GY._value)
print(GY.path)
print(GY.others)