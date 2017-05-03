# Design pattern practice
# Builder mode
# The difference between builder mode and abstract factory is
# that the process of builder mode is not solid. Orders of
# objects is ordered by a builder. Builder can combine all 
# requsets from client and return a special class.

# Enum using in python
# Enum('Enum name','object1 object2')
# object1=1, object2=2
from enum import Enum
import time

# Factory mode
MINI14='1.4GHz Mac mini'

class AppleFactory:
    # Nested class wont't be build when the class outside is builded
    class MacMin14:
        def __init__(self):
            # Values is defined inside the class, not the demand from client. 
            self.memory=4
            self.hdd=500
            self.gpu='Intel HD Graphics 5000'
        
        def __str__(self):
            info =  (   
                        'Model:{}'.format(MINI14),
                        'Memory:{}GB'.format(self.memory), 
                        'Hard Disk:{}GB'.format(self.hdd), 
                        'Graphics:{}'.format(self.gpu)
                    )
            return '\n'.join(info)
    
    def Build_Computer(self,model):
        if (model==MINI14):
            # Build the class inside the class
            return self.MacMin14()
        else:
            print ('I don\'t know how to build {}.'.format(model))

# Builder mode
class Computer:
    def __init__(self,serial_number ):
            # Only set the serial number at begining. 
            self.serial=serial_number
            self.memory=None
            self.hdd=None
            self.gpu=None
        
    def __str__(self):
        info=('Serial Number:{}'.format(self.serial),
                'Memory:{}GB'.format(self.memory), 
                'Hard Disk:{}GB'.format(self.hdd), 
                'Graphics:{}'.format(self.gpu))
        return '\n'.join(info)
    
    def Build_Computer(self,memory,hdd,gpu):
        self.memory=memory
        self.hdd=hdd
        self.gpu=gpu

class Computer_Builder:
    def __init__(self):
        self.Computer=Computer('J0023RT5')

    def configureMemory(self,memory):
        self.Computer.memory=memory

    def configureHardDisk(self,hdd):
        self.Computer.hdd=hdd

    def configureGPU(self,gpu):
        self.Computer.gpu=gpu

class HardwareEngineer:
    def __init__(self):
        # Initialize
        self.Computer_Builder=None
    
    def Construct_Computer(self,memory,hdd,gpu):
        self.Computer_Builder=Computer_Builder()
        [step for step in(  self.Computer_Builder.configureMemory(memory),
                            self.Computer_Builder.configureHardDisk(hdd),
                            self.Computer_Builder.configureGPU(gpu)
        )]

    @property
    def computer(self):
        return self.Computer_Builder.Computer

# Pizza practice

PizzaProgress=Enum('PizzaProgress','queued preparation baking ready')
PizzaDough=Enum('PizzaDough','thin thick')
PizzaSauce=Enum('PizzaSauce','tomato creme_fraiche')
PizzaTopping=Enum('PizzaTopping','mozzarella double_mozzarella bacon ham mushroom red_onion orengano')
STEP_DELAY=3

class Pizza:
    def __init__(self,name):
        self.name=name
        self.dough=None
        self.sauce=None
        self.topping=[]
    
    def __str__(self):
        return self.name

    def prepare_dough(self,dough):
        self.dough=dough
        print('preparing the {} dough of your {}...'.format(self.dough.name,self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))

class MargaritaBuilder:
    def __init__(self):
        self.pizza=Pizza('Margarita')
        self.progress=PizzaProgress.queued
        self.baking_time=5

    def prepare_dough(self):
        self.progress=PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)
    
    def add_sauce(self):
        print ('add the tomato szuce to your margartia...')
        self.pizza.sauce=PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print ('done with the tomato sauce')

    def add_topping(self):
        print ('adding the topping (double mozzarella, oregano) to your margarita')
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella,PizzaTopping.orengano)])
        time.sleep(STEP_DELAY)
        print ('done with the topping (double mozzarella,oregano)')

    def bake(self):
        self.progress=PizzaProgress.baking
        print ('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(STEP_DELAY)
        self.progress=PizzaProgress.ready
        print ('margarita is ready')


class NwewReceipeTwo:
    def __init__(self):
        self.pizza=Pizza('NewReceipeTwo')
        self.progress=PizzaProgress.queued
        self.baking_time=20

# Show progress of pizza in prepare_dough     
    def prepare_dough(self):
        # Pizza is preparing in this section
        self.progress=PizzaProgress.preparation
        # Prepare dough
        self.pizza.prepare_dough(PizzaDough.thin)

# Add sauce variable in class
    def add_sauce(self):
        # Pizza is still preparing
        self.pizza.sauce=PizzaSauce.creme_fraiche
        print ('add creme_fraiche in your {}'.format(self.pizza))
        time.sleep(STEP_DELAY)
        print ('done with creme fraiche sauce')
    
# Execute topping method in pizza class
    def add_topping(self):
        print ('adding topping to your {}'.format(self.pizza))
        # Add topping ingredients to the list
        self.pizza.topping.append([i for i in(PizzaTopping.double_mozzarella,PizzaTopping.red_onion)])
        time.sleep(STEP_DELAY)
        print ('done with topping adding')

# Show progress in  baking
    def bake(self):
        self.progress=PizzaProgress.baking
        print ('baking {} for {} second'.format(self.pizza,self.baking_time))
        time.sleep(self.baking_time)
        print('Your {} is ready'.format(self.pizza))

#class NewReceipeThree:
#    def __init__(self):
#        self




class NewReceipe:
    def __init__(self):
        self.pizza=Pizza('Special')
        # Pizza making is begining
        self.progress=PizzaProgress.queued
        self.baking_time=10
    
    def prepare_dough(self):
        # Pizza is preparing
        self.progress=PizzaProgress.preparation
        # Pizza's dough in NewReceipe is thin
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        self.pizza.sauce=PizzaSauce.creme_fraiche
        print ('add the creme fraiche sauce to your {}}...'.format(self.pizza))  
        time.sleep(STEP_DELAY)
        print ('done with creme fraiche sauce')

    def add_topping(self):
        print ('adding the topping (double mozzarella, oregano) to your margarita')
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella,PizzaTopping.orengano,PizzaTopping.orengano)])
        time.sleep(STEP_DELAY)
        print ('done with the topping (double mozzarella,oregano)')

    def bake(self):
        self.progress=PizzaProgress.baking
        print ('baking your {} for {} seconds'.format(self.pizza,self.baking_time))
        time.sleep(self.baking_time)
        self.progress=PizzaProgress.ready
        print ('your {} is ready'.format(self.pizza))

class Waiter:
    def __init__(self):
        self.builder=None
    
    def construct_pizza(self,builder):
        self.builder=builder
        [step() for step in(builder.prepare_dough,builder.add_sauce,builder.add_topping,builder.bake)]
    
    @property
    def pizza(self):
        return self.builder.pizza

# Factory mode
print ('================Factory Mode================')
# Class of mini14 isn't builded yet
afac=AppleFactory()
# Class of mini14 is builded now for return
# All hardwares were decided before
Mac_mini=afac.Build_Computer(MINI14)
print (Mac_mini)

# Builder mode
print ('================Builder Mode================')
Engineer=HardwareEngineer()
# User can get the hardware they want
Engineer.Construct_Computer(4,1000,'Geforce')
# This computer is loaded from class HardwareEngineer
conputer=Engineer.computer
print (conputer)

# Pizza pracitce
print ('================Pizza practice================')
builders=dict(m=MargaritaBuilder,n=NewReceipe,t=NwewReceipeTwo)
pizza_style=input('m or n or t ? ')
builder=builders[pizza_style]()
waiter=Waiter()
waiter.construct_pizza(builder)
pizza=waiter.pizza
print('Enjoy your {}!'.format(pizza))
