import re 


gmail = input("enter the gmail :: ")

m = re.findall("\S+@\S+",gmail)
print(m)




'''

Gmail - Any mail matching with above pattern


'''
N - Non space matching