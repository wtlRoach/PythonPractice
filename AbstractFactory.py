# Design pattern practice
# Abstract factory

class Frog:
    def __init__(self, name):
        self.name=name

    def __str__(self):
        return self.name
    # Remember add () when you're calling function
    def interact_with(self, obstacle):
        print ('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))

class Bug:
    def __str__(self):
        return 'a Bug'
    
    def action(self):
        return 'Eats it'

class FrogWorld:
    def __init__(self, name):
        print (self)
        self.player_name=name
    
    def __str__(self):
        return '\n\n\t---------Frog World---------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()

class GameEnviroment:
    def __init__(self, factory):
        # Get practical class (FrogWorld in here) and execute the function in this practical class
        self.hero=factory.make_character()
        self.obstacle=factory.make_obstacle()
    
    def play(self):
        self.hero.interact_with(self.obstacle)


game=GameEnviroment(FrogWorld('FU'))
game.play()
