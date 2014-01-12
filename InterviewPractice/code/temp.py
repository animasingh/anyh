class Critter2(object):
    def __init__(self,name, mood):
        self.name = name; # public
        self.__mood = mood; #private
        
    def talk(self):
        print "I'm {0}".format(self.name)
        print "I feel {0}".format(self.__mood)
    
    def __private_method(self):
        print 'This is a private method'
    
    def public_method(self):
        print "This is a public method"
        self.__private_method()


c = Critter2('anima','work')
d= Critter2('anisha','work')
c<d