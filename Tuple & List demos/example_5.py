# list comprehension

# old-fashioned 
my_list = []
for i in range(10):
    if i%2==0:
        my_list.append(i**2)
# comprehension
my_list_v2 = [i**2 for i in range(10) if i%2 == 0] 

print(f'my list is {my_list}')
print(f'my list v2 is {my_list_v2}')

