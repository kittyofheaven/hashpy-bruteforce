import time
import random
from urllib.request import urlopen, hashlib 
from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

characters = "012345689abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/.,!?-+<>"
characters_only = "012345689abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_only = "012345689abcdefghijklmnopqrstuvwxyz"
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
user_method_choice = input("your choice : ")
clear()

psswd_length = int(input("password length (insert 0 if u dont know) : "))
clear()

def cracking(methods, psswd_hash):
  methods_dict = {'1' : characters, '2' : characters_only, '3' : lowercase_only,}
  characters_list = list(methods_dict[methods])
  
  guess = ''
  hashed_guess = ''

  if psswd_length != 0 :

    while (hashed_guess != psswd_hash):
      guess = random.choices(characters_list, k=psswd_length)
      guess =''.join(guess)
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
    clear()

  elif psswd_length == 0 : 

    while (hashed_guess != psswd_hash):
      guess = random.choices(characters_list, k=int(psswd_length))
      guess =''.join(guess)
      print(guess)
      if int(hash_type) == 1 :
        print(guess)
        hashed_guess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
      elif int(hash_type) == 2 : 
        print(guess)
        hashed_guess = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
      else :
        print("user hash method choice invalid, try again!")
        exit()
    clear()

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