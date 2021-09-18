# MD5, SHA1 Brute forcer
hash brute forcer built in python 3
user can choose between hashing MD5 or hasing SHA1

## Instalation
```bash
$git clone https://github.com/kittyofheaven/hashpy-bruteforce.git 
$cd hashpy-bruteforce.git
$python bruteforce.py
```
## How to use ?
- install python3 on ur computer
- open up ur terminal and open bruteforce.py
- insert ur md5/sha1 hash
- choose methods
- enjoy !

## Methods
| Methods       |   char list   |
| ------------- | ------------- |
| All characters  | 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/.,!?-+<>  |
| Characters only  | 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ  |
| Lowercase only  | 0123456789abcdefghijklmnopqrstuvwxyz  |
| Numbers only  | 0123456789  |
| User defined chara  | your defined characters  |

## User defined characters
you can modify this section of bruteforce.py variable
```python3
#modify this variable
user_defined_chara = "input ur defined chara here" 
```
and choice 5 on choose method prompt
```bash
$ python3 bruteforce.py

choose method, all of this included number
1. all_characters (with symbol)
2. characters_only (with uppercase & lowercase)
3. lowercase_only (lowercase only)
4. numbers only 
5. user defined chara (setup tutor on https://github.com/kittyofheaven/hashpy-bruteforce)
your choice : 5
```
so that the bruteforce program only use characters on user defined variables

## About
author  **Shironeko** 

feel free to use this script as educational purpose ONLY ,i'll be not responsible for any action user do with this script

```python3
"""
author = shironeko 
website = github.com/kittyofheaven

feel free to use this script as educational purpose ONLY ,i'll be not responsible for any action user do with this script
"""
```
