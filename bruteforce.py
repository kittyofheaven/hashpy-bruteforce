import time
import random
from urllib.request import urlopen, hashlib 
from os import system, name
from time import sleep
from itertools import product

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/.,!?-+<>"
characters_only = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_only = "0123456789abcdefghijklmnopqrstuvwxyz"
numbers_only = "0123456789"
#list_of_common_password = str(urlopen())

user_psswd_hash = input('input hash to crack :')
clear()

print("choose hash type")
print("1. SHA1")
print("2. MD5\n")
hash_type = input("your choice :")
clear()

print("choose method, all of this included number")
print("1. all_characters (with symbol)")
print("2. characters_only (with uppercase & lowercase)")
print("3. lowercase_only (lowercase only)")
print("4. numbers only ")
user_method_choice = input("your choice : ")
clear()

psswd_length = int(input("password length (insert 0 if u dont know) : "))
clear()

def cracking(methods, psswd_hash):
  methods_dict = {'1' : characters, '2' : characters_only, '3' : lowercase_only, '4' : numbers_only}
  characters_str = methods_dict[methods]
  characters_list = list(methods_dict[methods])
  char_prod = product(characters_str, repeat = psswd_length)

  guess = ''
  hashed_guess = ''

  if psswd_length != 0 :
    
    for each_char in char_prod :
      if hashed_guess != psswd_hash :
        guess = ''.join(each_char)
        print(guess)
        if int(hash_type) == 1 :
          print(guess)
          hashed_guess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
        elif int(hash_type) == 2 : 
          print(guess)
          hashed_guess = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
        else :
          print("user hash method choice invalid try again")
          exit()
      else :
        break
      clear()     

  elif psswd_length == 0 : 

    dunno = 1
    while (hashed_guess != psswd_hash):

      for each_char in product(characters_str, repeat = dunno) :
        if hashed_guess != psswd_hash :
          guess = ''.join(each_char)
          print(guess)
          if int(hash_type) == 1 :
            print(guess)
            hashed_guess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
          elif int(hash_type) == 2 : 
            print(guess)
            hashed_guess = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
          else :
            print("user hash method choice invalid try again")
            exit()
        else :
          break
        clear()
      dunno += 1

  else :
    pass

  if hashed_guess == psswd_hash : 
    print("password match found! : " + guess)
  else :
    print("password hash not found :(")

cracking(user_method_choice, user_psswd_hash)





"""
author = shironeko 
website = github.com/kittyofheaven

feel free to use this script as educational purpose ONLY ,i'll be not responsible for any action user do with this script
"""
