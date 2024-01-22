import os
import time

def readfile () :
    with open ("new_file.txt" ,"r") as file : 
        print (file.read())

readfile()