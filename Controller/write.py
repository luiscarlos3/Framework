import re
import os, sys
class Console:     
    # valid entries only for numbers
    @staticmethod    
    def inputNumber(args):
        while True:
            var = input(args)
            try:
                var = int(var)
                return var
            except ValueError:    
                print("invalid")                                           
    #valid entries only for letters     
    @staticmethod
    def inputString(args):     
        while True:
            var = input(args)            
            if Console.__charactersNotNumber(var) == False and Console.__space(var) == True:                
                return var
            else:
                print("invalid")                
    #valid entries only for letters    
    @staticmethod           
    def inputDecimal(args):
        while True:
            var = input(args)
            try:
                var = float(var)
                return var
            except ValueError:
                print("invalid")
    #valid entries only for alphabetical      
    @staticmethod
    def inputAlpha(args):
        while True:
            var = input(args)
            if var.isalpha():
                return var
            else:
                print("invalid")            
    
    @staticmethod           
    def inputStringNumber(args):
        while True:
            var = input(args)
            if var.isdigit():
                return var
            else:
                print("invalid")
             
                 
    @staticmethod          
    def __charactersNotNumber(cadena):
        try:
            float(cadena)
            return True
        except (TypeError, ValueError):
            return False
        
    @staticmethod
    def __space(args):
        value = False
        charterlist = list(args)
        if not charterlist or charterlist[0] == " ":
            value = False
        else:
            value = True
        
        return value
    
    
            
        
        
        
        
            
        
        
            
        
    