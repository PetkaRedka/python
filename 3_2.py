def person_data(name, surname, birthyear, city, email, phone_number):
    
    return " ".join([name, surname, birthyear, city, email, phone_number])


print(person_data(
    name = input("Enter your name: "),
    surname = input("Enter your surname: "),
    birthyear = input("Enter your birthyear: "),
    city = input("Enter your city: "),
    email = input("Enter your email: "),
    phone_number = input("Enter your phone number: ")
))