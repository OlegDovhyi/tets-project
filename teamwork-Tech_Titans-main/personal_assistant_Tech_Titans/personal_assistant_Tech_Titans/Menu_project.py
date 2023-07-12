from task_11 import move_files
import json
from pogoda import pogoda_in_city
from pathlib import Path
import random
from os import listdir
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
from datetime import datetime, timedelta
from AddressBookBot import AddressBook
import AddressBookBot
import pickle
from pyowm import OWM
import NoteBook
import NoteBookBot
import time
import shutil




# def json_file(AddressBook,NoteBook):
#     with open('users_AddressBook.json', 'w') as fh:
#        json.dump(AddressBook,fh, indent=4, ensure_ascii=False)
#        print('AddressBook was creeate in json.')

#     with open('users_NoteBook.json', 'w') as fh:
#        json.dump(NoteBook,fh, indent=4, ensure_ascii=False)  
#        print('NoteBook was creeate in json.')

# def unpacked_AddressBook():
#     with open('users_AddressBook.json', 'r', encoding='utf-8') as read:
#        unpacked_users = json.load(read) 
#        print("AddressBook was unpacked.")
#        return unpacked_users
    
# def unpacked_NoteBook():  
#     with open('users_NoteBook.json', 'r', encoding='utf-8') as read2:
#        unpacked_users2   = json.load(read2) 
#        print("NoteBook was unpacked.")
#        return unpacked_users2


def menu ():
    while  True:
       print(' 1 - PhoneBook;\n 2 - NoteBook;\n 3 - SortFail;\n 4 - save PhoneBook,NoteBook;\n 5 - load PhoneBook,NoteBook;\n 6 - Wether;\n 7 - fun game')
       vodim = input("enter command: ")
       
       if vodim == '1':
            print ('start work in AddressBook: ')
            AddressBookBot.main()
              
        

       if  vodim == '2':
           print ('start work in NoteBook:')
           NoteBookBot.main()

              
       if vodim == '3':
            while True:
                path = Path(input('Enter the path of the folder where you want to sort files\n("Введіть путь папки де потрібно зробити сортування файлів"): '))
                if len(str(path)) <= 1:
                    print ("--You didn't lead anything, try another path\n   ('ви нічого не вели, спробуй другой шляx')\n--------------------------------------")
                    break 
                else :      
                    try:
                        move_files (path)
                    except :
                        print ('The path to the folder was not found\n ("Путь к папке не знайден")\n ------------------------------------------------------------------ ')
                        break

        
    #    elif vodim == '4':
    #          json_file( AddressBook ,NoteBook) 
        
    #    elif vodim == '5':
    #          unpacked_AddressBook()
    #          unpacked_NoteBook()

       elif vodim == '6':
            pogoda_in_city()

       elif vodim == '7':
              print('the game will start in 3 seconds')
              time.sleep(3)
              import mygame.main
              mygame.main

       elif  vodim.lower()  == 'close' or vodim.lower()  == 'exit':
            print("Good bye!")
            break
       else :
           print('To start the project, select numbers from the menu')

 
if __name__ == '__main__':
 menu ()