""" Write a Python program to get a dictionary from an object's fields.
"""
class dictobj(object):
    def __init__(self):
        self.Name = 'Khang'
        self.Age = 27
        self.Address = '4410 W Kent Ave'
    def do_nothing(self):
        pass
test = dictobj()
print(test.__dict__)