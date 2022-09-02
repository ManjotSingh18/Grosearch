'''
Created on Aug 18, 2022

@author: manjo
'''


# Custom Error class for products that are not found
class ItemNotFound(Exception):
    def __init__(self, item, message='Item Not Found'):
        self.item = item
        self.message= message
        super().__init__(self.message)
