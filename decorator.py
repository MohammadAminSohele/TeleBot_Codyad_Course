def my_decorator(func):
    def wraper():
        print('hello')
        func()
        print('good bye')
    return wraper

@my_decorator
def my_func():
    print('My name is Mohammad')

my_func()