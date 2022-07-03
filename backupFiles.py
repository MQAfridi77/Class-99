import os
import shutil

source = input("enter source folder name:- ")
destination = input('enter destination folder name:- ')

source = source + '/'
destination = destination + '/'

#os.listdir we get all the files from the source folder - - to store all files in list of files variable
list_of_files = os.listdir(source)
for file in list_of_files:
    #Copies all the files - source to destination
    shutil.copy((source+file), destination)
