bike = ['honda','pulsur','super','hero','yamha','ktm']
for i in bike:
    print(i,end='\n')
# print(i,end='\n')  ----------> indent error 
    print(i.title()+' is a good bike')
print('Pick your favorit bike')
print('Pick your favorit bike '+i.title())  # --> no indent error happen, it is a logical error

# s = 'Hello Akash Sahu'
#     print(s)
