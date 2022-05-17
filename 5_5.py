from random import randrange, randint

summ = 0

with open("file_5.txt", "w+") as my_file:
    
    for _ in range(randrange(10, 30)):
        my_file.write(f"{randint(1, 1000)} ")  
    my_file.seek(0)

    summ = sum([int(elem) for elem in my_file.read().split()])
    print(f"Summ: {summ}")
