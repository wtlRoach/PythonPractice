class Computer:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'the {} computer'.format(self.name)
    def execute(self):
        return 'Execute a program'

class Synthesizer:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'A {} synthesizer'.format(self.name)
    def play(self):
        return ' is playing a song '

class Human:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return '{} in the house'.format(self.name)
    def speak(self):
        return 'is speaking'

class Adapter:
    def __init__(self,obj,adapter_method):
        self.obj=obj
        self.name=obj.name
        self.__dict__.update(adapter_method)
    def __str__(self):
        return str(self.obj)    

def main():
    #Let objects be a list
    objects=[Computer('TEST')]
    synth=Synthesizer('moog');
    #Append synth into objects and add a characteristic named execute, and point to play method
    objects.append(Adapter(synth,dict(execute=synth.play)))
    human=Human('Tim');
    #Append human into objects and add a characteristic named execute, and point to speak method
    objects.append(Adapter(human,dict(execute=human.speak)))

    for i in objects:
        print('{} {}'.format(str(i),i.execute()))
    #The name in adapter is the name in every different object, not adapter itself
    for i in objects:
        print(i.name)

if __name__=="__main__":
    main()

#Print all characteristic of Computer
#print(Computer.__dict__)