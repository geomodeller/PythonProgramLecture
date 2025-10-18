from random import randint

my_results = []
for i in range(100_000_000):
    dice = randint(1, 6)
    my_results.append(dice)

print(f'Probability for dice to have "1" is {my_results.count(1)/len(my_results)*100:.7f}%')