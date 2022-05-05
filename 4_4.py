# from random import randrange, randint

# start_list = [randint(0, 100) for i in range(randrange(10, 20))]
# print("Start list: ", satrt_list)

start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [elem for elem in start_list if start_list.count(elem) == 1]
print(new_list)
