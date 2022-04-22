words = input("Enter some words: ").split()

for i in range(len(words)):
       
    print(f"{i}) {words[i][:10:]}")