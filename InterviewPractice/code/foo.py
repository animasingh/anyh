import pprint
class Foo(object):
    class_attr=0
    
    def __init__(self, item):
        self.instance_attr=item
    
    def report(self):
        print "My class_attr is {0}".format(self.class_attr)
        print "My __class__.class_attr is {0}".format(self.__class__.class_attr)
        print "My instance_attr is {0}".format(self.instance_attr)
        
    def print_self_dict(self):
        pprint.pprint(self.__dict__)
        
    def change_class_attr(self,item):
        self.__class__.class_attr = item