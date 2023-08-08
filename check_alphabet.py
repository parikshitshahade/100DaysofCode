import string
alphabet = list(string.ascii_letters) #a part of string library which contains all the alphabets lowercase and uppercase too)
x = input("Enter your alphabet:") 
if (x in alphabet):
    print("Alphabet")
else:
    print("Not an alphabet")
