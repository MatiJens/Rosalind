with open ("txt/rosalind_fib.txt", "r") as f:
    data = f.read().split()
    months,newOffspring = int(data[0]), int(data[1])
    adultRabbits = 1
    youngRabbits = 0
    for i in range(months - 1):
        rabbits = adultRabbits + youngRabbits
        youngRabbits = adultRabbits * newOffspring
        adultRabbits = rabbits
print(rabbits)

