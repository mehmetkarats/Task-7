import os
import time 

def writefile ():
    data = input ("Enter the data you want to save:" )
    file= open("new_file.txt" , "a")
    file.write (data +"\n")
    file.close()

writefile ()

