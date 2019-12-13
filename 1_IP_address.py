import re 

ip_address = input("Enter the ip_address ::  ")

m = re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",ip_address)

print(m)




'''

Error: AttributeError

  File "Practice.py", line 6, in <module>
    print(m.group())
AttributeError: 'list' object has no attribute 'group'
'''

ip address is keep on changing here minimum 1 and minimum 3 will come for Ip_address

ip_addresss: list 

1.123.12.1
123.25.12.1
2.0.25.321

'''
https://lite.ip2location.com/india-ip-address-ranges

u will get the ip_address patterns through the above url
'''

