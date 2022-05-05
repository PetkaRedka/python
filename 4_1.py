from sys import argv

if (len(argv) != 4):
    print("Wrong number of the arguments! It has to be 3!")

else:

    production, rate, premium = argv[1::]
    try:
        print(f"Total wage: {float(production) * float(rate) + float(premium)}")

    except ValueError:
        print("All values have to be numbers!")