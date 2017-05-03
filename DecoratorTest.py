def Foo(func):
    def wrap():
        print ('After decorate.')
        func()
        print ('After decorate.')
    #Only return function name
    return wrap

def Qoo(func):
    def wrap():
        print ('Second decorate.')
        func()
        print ('Second decorate.')
    #Only return function name
    return wrap

@Foo
@Qoo
def bar():
    print ('bar')

bar()