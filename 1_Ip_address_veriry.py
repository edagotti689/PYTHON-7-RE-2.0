#12) IP address matching using regular expressions

# id = '192.168.2.10'     ###it is fine not getting error


import re


ip_address = input('enter a address to validate:')

m = re.fullmatch('\d{3}.\d{3}.[0-9]?.[0-9]{2}',ip_address)

if m!=None:
    print('It is a valid ip address',ip_address)
    
else:
    print('It is not a valid ip address',ip_address)
    