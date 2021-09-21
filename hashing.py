import hashlib #,bcrypt #install bcrypt first on ur python
print(r"""_  _  __  ____ _  _   ____ _  __   
/ )( \/ _\/ ___/ )( \ (  _ ( \/ )  
) __ /    \___ ) __ (_ ) __/)  /  
\_)(_\_/\_(____\_)(_(_(__) (__/    
by : kittyofheaven
""")
psswd = input("input password to hash : ")

def sha1_encrypt():
  print("\nSHA1\n")
  setpsswd = bytes(psswd, 'utf-8')
  hash_object = hashlib.sha1(setpsswd).hexdigest()
  print(hash_object)

def md5_encrypt():
  print("\nMD5\n")
  setpsswd = bytes(psswd, 'utf-8')
  hash_object = hashlib.md5(setpsswd).hexdigest()
  print(hash_object)

#def bcrypt_encrypt():
  #print("\nBCRYPT\n")
  #setpsswd = bytes(psswd, 'utf-8')
  #hash_object = bcrypt.hashpw(setpsswd, bcrypt.gensalt(10))
  #print(hash_object)

print("methods to choose : \n")
print("1. SHA1")
print("2. MD5")
#print("3. BCRYPT")
methods = input('ur methods :')

if int(methods) == 1 :
  sha1_encrypt()
elif int(methods) == 2 :
  md5_encrypt()
#elif int(methods) == 3 :
  #bcrypt_encrypt()
else :
  print('there is no that methods aborting...')


"""
author = shironeko 
website = github.com/kittyofheaven

feel free to use this script as educational purpose ONLY ,i'll be not responsible for any action user do with this script
"""