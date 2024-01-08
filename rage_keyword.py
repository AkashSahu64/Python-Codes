# for i in range(5,11):
for i in range(11):
    print(i)

number = list(range(11))
print(number)
even_number = list(range(2,11,2))
print(even_number)

square = []
for i in range(1,11):
    # value = i**2
    square.append(i**2)
print(square)

# num = [1,2,3,4,5,6,7,8,9,0]
print(min(square))
print(max(square))
print(sum(square))
# list comprehension
s_num = [i**2 for i in range(1,11)]
print(s_num)
# slicing the list
print(s_num[0:5])
print(s_num[4:])
print(s_num[:3])
print(s_num[2:6])
print(s_num[-3:])
print(s_num[:-4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())