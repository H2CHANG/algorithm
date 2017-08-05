import random
'''
male = [[2, 6, 5, 9, 1, 8, 0, 7, 4, 3], [4, 3, 6, 8, 7, 1, 0, 9, 5, 2], [2, 4, 0, 9, 1, 3, 6, 8, 7, 5], [5, 7, 1, 9, 2, 8, 0, 3, 4, 6], [1, 3, 0, 5, 7, 4, 8, 6, 9, 2], [0, 3, 2, 5, 7, 8, 9, 6, 1, 4], [1, 4, 2, 9, 0, 7, 6, 8, 5, 3], [6, 4, 5, 9, 1, 2, 7, 3, 8, 0], [9, 2, 7, 3, 4, 5, 1, 6, 8, 0], [9, 2, 0, 6, 4, 5, 8, 3, 7, 1]]

female = [[9, 1, 8, 2, 4, 7, 6, 0, 3, 5], [4, 9, 6, 2, 5, 3, 1, 0, 7, 8], [6, 0, 1, 9, 8, 4, 2, 7, 3, 5], [6, 3, 2, 8, 9, 1, 5, 4, 0, 7], [6, 7, 4, 3, 8, 2, 9, 1, 5, 0], [6, 7, 5, 2, 4, 8, 1, 0, 3, 9], [6, 2, 9, 7, 0, 4, 1, 5, 8, 3], [0, 7, 8, 1, 2, 3, 5, 4, 9, 6], [8, 0, 3, 5, 4, 1, 9, 2, 7, 6], [3, 1, 8, 2, 6, 4, 7, 5, 9, 0]]
'''

male = []
female = []
for i in range(0,100):
    random_list = random.sample(range(100), 100)
    male.append(random_list)

for i in range(0,100):
    random_list = random.sample(range(100), 100)
    female.append(random_list)


#print("male", male)
#print("female", female)
male_engage = [20] * 100
female_engage = [30] * 100


#every male must be paired
while 20 in male_engage:
    male_index = 0
    #female_index = 0
    for i,num in enumerate(male_engage):
        if num == 20:
            male_index = i
            #print("i", i)
            break

    #loop every male
    while len(male[male_index]) != 0:
        female_index = male[male_index].pop(0)
        #print("male index", male_index)
        ##print("female index", female_index)
        #print("female_engage[female_index] ", female_engage[female_index] )

        #print("female[female_index].index(male_index)", female[female_index].index(male_index))
        #print("female[4]", female[4])
        #print("female", female)
        #print("female[female_index]", female[female_index])
        #print("female[female_index],idex", female[female_index].index(male_index))

        #if female not engaged
        if female_engage[female_index] == 30:


            male_engage[male_index] = female_index
            female_engage[female_index] = male_index
            break
        #if fmale engaged
        elif female_engage[female_index] != 30:

            male_temp_index = female_engage[female_index]

            # more preference before
            if male_temp_index < male_index:
                continue
            #less preference before
            else:

                male_engage[male_temp_index] = 20

                male_engage[male_index] = female_index
                female_engage[female_index] = male_index
                break



print(male_engage)
print(female_engage)






