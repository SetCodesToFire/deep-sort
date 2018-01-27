import random
inputgen=[9,8,7,6,5,4,3,2,1,0]
thefile = open('input.txt', 'w')

for i in range(5000):
    random.shuffle(inputgen)
    for item in inputgen:
        thefile.write("%s," %item)
    thefile.write("\n")
