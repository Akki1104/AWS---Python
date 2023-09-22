dict = {
    "apple": "A Fruit",
    "computer": "An Electronic",
    "python": "A Programming Langauge",
    "ocean": "A Vast Water Body"
}

def search_word(word):
    return dict.get(word.lower(), "Word Not Found.")

while True:
    user_input = input("Enter a word to get its meaning ( or 'q' to quit): ")
    
    if user_input == 'q':
        print("GoodBye")
        break

    meaning = search_word(user_input)
    print(meaning)