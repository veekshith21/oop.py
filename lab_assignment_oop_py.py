# -*- coding: utf-8 -*-
"""lab assignment.oop.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n3xMDMvmyNfYZ_edSlqggVIA9XIWEd58
"""

#@title Problem 1
year = int(input("Enter the Year: "))

def checkyear(year):
  if(year%400 == 0):
    print('It is a leap year')
    return(True)
    
  elif(year%4==0 and year %100 != 0):
    print('It is a leap year')
    return(True)
    
  else:
    print('It is not a leap year')
    return(False)
    
checkyear(year)

#@title Problem 2
n = int(input("Enter a number: "))
if(n%2 != 0):
  print("Weird")  
elif(n%2 == 0):
  if(n>= 2 and n<=5):
    print("Not Weird")
  if(n>=6 and n<=20):
    print("Weird")
  if(n>20):
    print("Not Weird")

#@title Problem 3
n = int(input("Enter the number of guests: "))
guests = []
for i in range(0, n):
  name = str(input("enter the name of guests: "))
  guests.append([name])
print("Guests are: ", guests)
if(n%2==0):
  for k in range( int((n)/2) , n-1):
    print("\nFashionable late persons are: ", guests[k])
elif(n%2 != 0):
  for k in range( int((n-1)/2) , n-1):
    print("\nFashionable late persons are: ", guests[k])

#@title Problem 4
def word_search_2(title_list, keyword):
    # make lowercase and remove punctuation
    keyword = keyword.lower().strip('.,')

    result_list = []
    for i, title in enumerate(title_list):
        # make lowercase and remove punctuation, then split into words
        words = title.lower().strip('.,').split()

        if keyword in words:
            result_list.append((i, title))

    return result_list

if __name__ == '__main__':
    docs = ['The Learn Python Challenge by Mahi','El do-rado','The mysterious house','Casinoville?',]
    w = 'house'

    print(word_search_2(docs, w))

#@title Problem 5
BP = float(input("Enter the Basic Pay: "))
DA = (40*BP)/100
HRA = (20*BP)/100
GP = BP + DA + HRA
print('Gross pay is:',GP)