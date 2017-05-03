import copy
from collections import OrderedDict

class Book:
    # Containing of parameters with ** must be a group 
    def __init__(self,name,author,price, **rest):
        self.name=name
        self.author=author
        self.price=price
        # Put other objects in the dict
        self.__dict__.update(rest)

    def __str__(self):
        mylist=[]
        # If not use OrderDict, the output would be different in every execute
        ordered=OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}:{}'.format(i,ordered[i]))
            if i=='price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)

class Prototype:
    def __init__(self):
        self.object=dict()

    def register(self,identifier,obj):
        self.object[identifier]=obj
    
    def unregister(self,identifier,obj):
        del self.object[identifier]

    def clone(self,identifier,**attr):
        found=self.object.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier:{}'.format(identifier))
        obj=copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

def main():
    # Using variables to initialize class
    b1=Book('A book',author=('cock','and cock'),price=1000,Information=('Second Ed.','No comment'),data='1985/10/9')
    prototype=Prototype()
    cid='First'
    prototype.register(cid,b1)
    b2=prototype.clone(cid,name='WTF Second Ed')
    for i in (b1,b2):
        print(i)
    print("ID b1:{}!=ID b2:{}".format(id(b1),id(b2)))

if __name__=='__main__':
    main()


#B1 = Book('A_Book','TA','100',test=('First edition','WTF'))
#print ('{}'.fromat(B1))
