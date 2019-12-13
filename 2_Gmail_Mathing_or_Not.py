#11) Gmail id matching using regular expressions # krishnamraju105@gmail.com

### I have a Doubt



import re


gmail = input('enter mail id to validate : ')
m = re.fullmatch('\w{12}\d{3}@[a-z]{5}.\w{3}',gmail)

if m!= None:
    print('It is a valid mail id', gmail)

else:
    print('it is not a valid mail id', gmail)



