import threading
import requests as rq 
import time
import random

characters = "012345689abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/.,!?-+<>"
characters_only = "012345689abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_only = "012345689abcdefghijklmnopqrstuvwxyz"

print("choose method, all of this included number")
print("1. all_characters (with symbol)")
print("2. characters_only (with uppercase & lowercase)")
print("3. lowercase_only (lowercase only)")

user_method_choice = input("your choice : ")
psswd_length = input("password length (insert 0 if u dont know) : ")
psswd = '12'

def cracking(methods):
  methods_dict = {'1' : characters, '2' : characters_only, '3' : lowercase_only,}
  characters_list = list(methods_dict[methods])
  guess = ''

  if psswd_length != 0 :
    while (guess != psswd):
      guess = random.choices(characters_list, k=int(psswd_length))
      guess =''.join(guess)
      print(guess)

cracking(user_method_choice)
