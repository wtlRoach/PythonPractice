"""
三個引號可以做為字串並保留其中的縮排
也可以取代#當註解，優點是可以多行註解
"""
from datetime import datetime
from random import randint

# coding=UTF-8

now=datetime.now()
def BasicFunction(input):
    encoded = input.encode('utf8')
    output = input
    print (output)
    print (' \n')

def DateTime():
    print ('Year:%s'%(now.year))
    print ('Month:%s'%(now.month))
    print ('Day:%s'%(now.day))
    print ('Date time:'+"%s/%s/%s" % (now.year,now.month,now.day))
    print (' \n')

def StringTestFunction():
    WordIndex=2
    StringTestMatrix="Test words inside"
    WordGetVariable=StringTestMatrix[WordIndex]
    print ('Word in index %s:%s'%(WordIndex,WordGetVariable))
    print ('Word in upper:%s'%(WordGetVariable.upper()))
    print ('Word in lower:%s'%(WordGetVariable.lower()))
    #其實也可以直接印不用str轉換
    #print ('Word index now:%s'%(str(WordIndex)))
    #但是用在字串相加需要先轉換
    print ('Word index now:'+str(WordIndex))
    print ('Here is the string in matrix:'+ '\n' + StringTestMatrix)
    print (' \n')

def LoopTestFunction():
    StringMatrix="Loop test matrix words"
    CharToSearch='o'
    Counter=0
    Variety=0
    for CharInMatrix in StringMatrix:
        if(CharInMatrix==CharToSearch):
            Variety=1
        else:
            Variety=0
        Counter=Variety+Counter
    print ('Number of word %s in StringMatrix is %s'%(CharToSearch,Counter))
    print (' \n')

def ListTestFunction():
    NumberList=[1,4,10,8,3,7]
    StringList=['A','B','C','D']
    PrintIndexStart=0
    PrintIndexEnd=4
    StringToFind='C'
    InsertString='X'
    InsertIndex=1
    StringToDelete='X'
    print ('String in StringList:\n')
    for String in StringList:
        print (String+'\n')
    StringList.append('E')
    print ('String in StringList after append \'E\':\n')
    for String in StringList:
        print (String+'\n')
    print ('List in StringList from index %s to %s:\n'%(PrintIndexStart,PrintIndexEnd))
    print(StringList[PrintIndexStart:PrintIndexEnd])
    print('\n')
    print('List all elements in StringList after index %s:\n'%(PrintIndexStart))
    print(StringList[PrintIndexStart:])
    print('List all elements in StringList before index %s:\n'%(PrintIndexEnd))
    print(StringList[:PrintIndexEnd])
    TargetIndex=StringList.index(StringToFind)
    print('Char %s is in index %s of StringList\n'%(StringToFind,TargetIndex))
    StringList.insert(InsertIndex,InsertString)
    StringList.insert(InsertIndex+1,InsertString)
    StringList.insert(InsertIndex+2,InsertString)
    print('Insert %s to index %s, %s and %s\n'%(InsertString,InsertIndex,InsertIndex+1,InsertIndex+2))
    print('StringList elements:\n')
    print(StringList)
    print('NumberList elements:\n%s\n'%(NumberList))
    NumberList.sort()
    print('After sort:\n%s\n'%(NumberList))
    StringList.remove(StringToDelete)#一次砍一個
    print('Remove %s in StringList\n'%(StringToDelete))
    print ('String in StringList:\n')
    print (StringList)

def DictionaryTestFunction():
    NumberDictionary={'Seafood':10,'Carrot':2,'Others':20}
    NewDictionary={}
    TargetKey='Seafood'
    NewKey='Pork'
    NewKeyValue=7
    StringKey='Data_Label'
    StringMatrixInDictionary={'I','J','K'}
    NumberKey='Data_Value'
    NumberMatrixInDictionary={5,20,1}
    print ('Value in NumberDictionary:\n')
    print (NumberDictionary)
    TargetKeyValue=NumberDictionary[TargetKey]
    print ('Value of key %s is %s\n'%(TargetKey,TargetKeyValue))
    print ('Values in NewDictionary:\n')
    print (NewDictionary)
    NewDictionary[NewKey]=NewKeyValue
    print ('Add new key %s and value %s'%(NewKey,NewKeyValue))
    print ('Values in NewDictionary:\n')
    print (NewDictionary)
    TotalLength=len(NewDictionary)
    print ('Total length of dictionary NewDictionary is %s\n'%(TotalLength))
    del NewDictionary[NewKey]#一看就知道一次砍一個
    print ('Delete key %s in NewDictionary\n'%(NewKey))
    print ('Values in NewDictionary:\n')
    print (NewDictionary)
    NewDictionary[StringKey]=StringMatrixInDictionary
    print ('Add new string matrix %s in key %s'%(StringMatrixInDictionary,StringKey))
    print ('Values in NewDictionary:\n')
    print (NewDictionary)
    NewDictionary[NumberKey]=NumberMatrixInDictionary
    print ('Add new string matrix %s in key %s'%(NumberMatrixInDictionary,NumberKey))
    print ('Values in NewDictionary:\n')
    print (NewDictionary)
    #NewDictionary[NumberKey].sort()不能直接srot?????因為加入字典裡自動sort好了??????
    #print ('Sort NumberMatrixInDictionary\n')
    DeleteNumber=1
    NewDictionary[NumberKey].remove(DeleteNumber)
    print ('Delete value %s in matrix of key %s'%(DeleteNumber,NumberKey))
    print ('Values in NewDictionary of key %s'%(NumberKey))
    print (NewDictionary[NumberKey])

def TestField():
    print (range(5))
    print (range(0,5))
    print (range(0,5,2))
    print (range(5,0,-1))
    print (list(range(5)))
    print (list(range(0,5)))
    print (list(range(0,5,2)))
    print (list(range(5,0,-1)))

def BattleShip():
    board=[]#Empty list
    for index in range(5):
        #Put ["O","O","O","O","O"] in board five times
        board.append(["O"]*5)
    #Show board
    for row in board:
        #print" "and insert elements from board
        print (" ".join(row))
    #Hide battle ship in random
    ShipPosition_Row=randint(0,len(board)-1)
    ShipPosition_Column=randint(0,len(board)-1)
    #Input Row and Columns for guessing
    #Function input is not work in Visual Code. It's necessery to run
    #the script from command line when interact with program
    Guess_Row=int(input("Row:"))# Comment out it when run in Visual Code
    Guess_Col=int(input("Col:"))# Comment out it when run in Visual Code
    #Debuging
    #print (ShipPosition_Row)
    #print (ShipPosition_Column)
    if ShipPosition_Row==Guess_Row:
        print ("Correct Row.")
        if ShipPosition_Column==Guess_Col:
            print ("Correct Column.")

def LoopFunction(InputNumber):
    Count=0
    #Don't let if-else statement do nothing
    # If there is nothing to do, skip it like following code 
    if Count<10:
        print ("Counter value is %s in if-else loop"%(Count))
    #Just skip the  else statement
    #else:
        
    while Count<10:
        print ("Counter value is %s"%(Count))
        Count+=1
    
    print("Number input:%s"%str(InputNumber))
    NumberInside=[]
    RemainNumber=InputNumber
    #Only the length of string can be calculated 
    NumLength=len(str(RemainNumber))
    NumberPosition=NumLength
    for index in range(NumLength):
        #Use int to delete numbers after point
        NumberInside.append(int(RemainNumber/(10**(NumberPosition-1))))
        #print(list(NumberInside))
        RemainNumber-=int((RemainNumber/(10**(NumberPosition-1))))*(10**(NumberPosition-1))
        #print (RemainNumber)
        NumberPosition-=1
        #print (NumberPosition)
    print (list(NumberInside))

def AdvancedPython():
    # Using function call elements in TestDictionary
    TestDictionary={
        "One":1,
        "Two":2,
        "Three":3
    }
    # Call keys and values
    print (TestDictionary.items())
    # Call keys
    print (TestDictionary.keys())
    # Call values
    print (TestDictionary.values())
    # Print keys and values
    # elements:keys
    # TestDictionary[elements]:values
    for elements in TestDictionary:
        print (elements, TestDictionary[elements])
    # Create List with a condition which all elements are even number 
    #listname=[(element in list)(examination)]
    TestListCondition=[element for element in range(50) if element%2==0]
    print (TestListCondition)
    # Print List with index condition
    # [start index:end index:index distance]
    TestNumberList=range(10)
    TestString='Test string'
    print (list(TestNumberList[::2]))
    print (list(TestNumberList[:2]))
    print (list(TestNumberList[2:]))
    print (list(TestNumberList[1:9:2]))
    # Reverse index (Like ring buffer)
    print (list(TestNumberList[::-1]))
    # String length test
    print (list(TestString[0:6:1]))

def Testlambda(x):
    # Test for lambda
    return lambda y: y+x
    
def ApplicationOfLambda(x):
    return filter(lambda x:x%2==0,range(1,x))

def TestAnonymousFunction(x):
    # In Visual code, the better way to use lambda is using them in a subfunction
    # and print or do other things in the main function
    # Anonymous function : lambda
    # Store value x for 40 and anonymous fumction is named ValueOfLambdaTest
    ValueOfLambdaTest=Testlambda(x)
    # Execute function ValueOfLambdaTest(y) below
    print (ValueOfLambdaTest(0))
    print (ValueOfLambdaTest(1))
    print (ValueOfLambdaTest(5))
    # Using filter and lambda to extract even number
    EvenNumbersFromOneToX=ApplicationOfLambda(x)
    print (list(EvenNumbersFromOneToX))


def IteratingOverDictionaries():
    Chess={
        "King":1,    
        "Queen":1,
        "Bishop":2,
        "Knight":2,
        "Rook":2,
        "Pawn":8,
        "Victory":"Check opponent and without way to escape"
    }
    print (Chess.items())

def BitOperation(x):
    print ("x>>1=%s"%str(x>>1))
    print ("x>>2=%s"%str(x>>2))
    print ("x&1=%s"%str(x&1))
    print ("x&2=%s"%str(x&2))
    print ("x|1=%s"%str(x|1))
    print ("x|2=%s"%str(x|2))
    print ("x^1=%s"%str(x^1))
    print ("x^2=%s"%str(x^2))
    # Variable x is a signed value
    print ("~x=%s"%str(~x))
    # Binary
    print ("0b1=%s"%str(0b1))
    print ("0b10=%s"%str(0b10))
    print ("0b11=%s"%str(0b11))
    # Binary transform
    print ("bin(1)=%s"%str(bin(1)))
    print ("bin(2)=%s"%str(bin(2)))
    print ("bin(3)=%s"%str(bin(3)))
    # Second parameter of int()
    print ("int(\"1\",2)=%s"%str(int("1",2)))
    print ("int(\"101\",2)=%s"%str(int("101",2)))
    print ("int(\"0b101\",2)=%s"%str(int("0b101",2)))
    print ("int(0b101)=%s"%str(int(0b101)))

class PythonClassTest(object):
    What_is_the_smell="Good" 
    # __init___ has two underlines at begin and end
    def __init__(self, Name, Color, Smell):
        self.Name=Name
        self.Color=Color
        self.Smell=Smell
    # Parameters must be called by self
    def SelfIntro(self):
        print ("Hi, I'm %s, my favorite color is %s, and I semll %s"%(self.Name,self.Color,self.Smell))
    # If a method need to use global variables, add self as a parameter
    def SelfSmellTest(self):
        if self.What_is_the_smell=="Good":
            print ("Pass")
        else:
            print ("Shit")
            
# Inheritance
class PythonClassTestSpecial(PythonClassTest):
    # Override
    def SelfSmellTest(self):
        if self.What_is_the_smell=="Bad":
            print ("Pass")
        else:
            print ("Shit")
    # Extend
    def SelfColorTest(self):
        if self.Color=="Black":
            print ("Nothing")
        else:
            print ("Color")

class FileIOTest(object):   
    def WriteDataToFile():
        my_list = [i**2 for i in range(1,11)]
        # If file is not in the directory, then this function will create it.
        FileWrite = open("PythonLoadFileTest.txt", "w")
        FileRead = open("output.txt", "r")
        #FileRead = open("output.txt","r+w")
        for item in my_list:
                FileWrite.write(str(item) + "\n")
        print ("Read data:\n")
        print (FileRead.read())
        FileWrite.close()
        FileRead.close()
    def ExecuteIOUsingWith():
        # When a object is used by "with", __enter__() in object is called and return
        # value to variable after "as". Atfer finished program or program throw any 
        # error message in "with", __exit__() of object will be called. 
        # So there is no need to call close() in the end of IO execution.
        with open("PythonLoadFileTest.txt", "w") as my_list:
            my_list.write("ExecuteIOUsingWith was executed");

def Recursive(n):
    if n==1:
        return n
    return n*Recursive(n-1)


BasicFunction('Basic Function Test')
DateTime()
StringTestFunction()
LoopTestFunction()
ListTestFunction()
DictionaryTestFunction()
# Function input can't be used in Visual Code 
# BattleShip()
LoopFunction(5236)
AdvancedPython()
IteratingOverDictionaries()
TestAnonymousFunction(20)
BitOperation(16)
Myself=PythonClassTest("Bill","Black","Good")
yourself=PythonClassTestSpecial("Ill","White","Bad")
# Objects in class can be used by outside since you can get the practical class
#print ("Hi, I'm %s, my favorite color is %s, and I semll %s"%(Myself.Name,Myself.Color,Myself.Smell))
Myself.SelfIntro()
yourself.SelfIntro()

Myself.SelfSmellTest()
yourself.SelfSmellTest()

yourself.SelfColorTest()
# I/O test
IOTest=FileIOTest()
FileIOTest.WriteDataToFile()

# Recursive
print (Recursive(10))


