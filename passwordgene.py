import random

upperCase = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
lowerCase = "abcdefghiklmnoprstuvwxyz"
specialCaracter = "&é(-è_çà)=*$ù!:;"


print("How many caracter you want : ")
nbrCaracter = int(input())

division = int(nbrCaracter/4)
password = ""

while nbrCaracter > division:
      randomUpperCase = random.randint(0, 23)
      randomLowerCase = random.randint(0, 23)
      randomSpecialCaracter = random.randint(0, 15)
      number = str(random.randint(0, 9))
      randomCara = upperCase[randomUpperCase] + lowerCase[randomLowerCase] + specialCaracter[randomSpecialCaracter] + number
      password = password + randomCara
      nbrCaracter = nbrCaracter - 4

print("Your password : "+ password)
