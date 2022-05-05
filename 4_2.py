from random import randrange, randint

old_list = [randint(0, 1000) for i in range(randrange(10, 20))]
print("Old list: ", old_list)

new_list = [old_list[i] for i in range(1, len(old_list)) if old_list[i] > old_list[i - 1]]
print("New list: ", new_list)