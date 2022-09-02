'''
Created on Aug 16, 2022

@author: manjo
'''

#A deprecated output tester before site was established
def TestOutput(products):
    for product in products:
        try:
            if product['averageRating']:
                print(product['name'], '$'+str(product['priceInfo']['currentPrice']['price']),'|', str(product['averageRating'])+'*')
            else:
                print(product['name'], '$'+str(product['priceInfo']['currentPrice']['price']))     
        except:
            print('Encoding Error')

