def int_func(word):

    alphabet = [chr(i) for i in range(97,123)]

    for i in range(len(word)):
        if word[i] not in alphabet:
            return "Only lattin small letters!"

    return word.capitalize()
         

words = input("Enter words: ").split()
for i in range(len(words)):
    words[i] = int_func(words[i])

print(" ".join(words))