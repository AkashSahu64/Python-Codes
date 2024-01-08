age = 12
if age < 4:
        price = 0
elif age<18:
        price = 5
else:
        price = 10
print(str(price))

avail = ['pizza', 'burgur','frech fry','noodle','coke','chees']
order = input([])
for i in avail:
        if i in order:
                print("Adding "+i)
        else:
                print("Sorry we don't have "+i)