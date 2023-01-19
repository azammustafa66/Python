import random

word_list = ['camel', 'dog', 'cat']
word = ""
word += random.choice(word_list)

display = []
for i in word:
    display += "_"

end = False
while not end:
    guess = input("Enter a letter: ").lower()

    for j in range(len(word)):
        if word[j] == guess:
            display[j] = word[j]
    print(display)

    if "_" not in display:
        end = True
        print("You win")
