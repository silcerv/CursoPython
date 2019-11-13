# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:17:45 2019

@author: Infocentro5
"""


class OperadorMates(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
    def suma  (x, y):
        return ("la suma es", x + y )
       
    def division ( x, y):
        return ("la division es ", x / y)
        
    def resta (x, y):
        return ("la resta es", x - y)
       
    def multiplicacion ( x, y):
       return ("la multiplicacion es", x * y)
   

    



#parser = argparse.ArgumentParser()
#parser.add_argument("-i1", "--integer1", type=int, default=50, required=False)
#parser.add_argument("-i2","--integer2", type=int, default=100, required=False)
#parser.add_argument("-i3", choices=['suma', 'division', 'resta', 'multiplicacion'], type=str, required= False)
#
#args = parser.parse_args()
#
##print(args.integer1)
#x = args.integer1
#print(x)
#
##print(args.integer2)
#y = args.integer2
#print(y)
#
#s = args.i3
#print(s)

#oper = args.i1
#print (oper)

#x = args. i1
#y = args. i2

#resultado = OperadorMates.suma(x , y)
#print (resultado)
#resultado2= OperadorMates.resta(x, y)
#print (resultado2)
#resultado3= OperadorMates.division(x, y)
#print (resultado3)
#resultado4= OperadorMates.multiplicacion(x, y)
#print (resultado4)