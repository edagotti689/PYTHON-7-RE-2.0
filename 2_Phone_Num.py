'''
Phone Number:

Find the Phone number is matching or not :

Ex: Phone Number Patterns(Indian phone numbers)

+91 1234567890
  0 1234567890
    1234567890

'''
import re 

Phone_num = input("Enter the valid number :: ")

m = re.findall("\d{10}", Phone_num)   # correct it 
# or

# m = re.findall("[+91|0|]*\d{10}", Phone_num)  # doubt on this 

print(m)