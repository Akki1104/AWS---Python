dictionary = {
    'a': ["Alive","Avid","Abecedarian","Affable","Adventurous","Acerbic","Adept","Admirable","Angelic","Animation","Acclaim","Adaptable"],
    'b': ["Balmy","Brave","Beautiful","Benevolent","Baggy","Babka","Beat","Blessed","Bashful","Banal","Beaming","Boisterous"],
    'c': ["Clean","Clear","Capable","Careful","Civil","Complex","Content","Charming","Clever","Certain","Cabal","Caring"],
    'd': ["Daisy","Daily","Dandy","Dally","Daffy","Dazed","Davit","Darcy","Daman","Damar","Daric","Doubt"],
    'e': ["Ease","Eager","Earn","Easily","Easy","Easygoing","Ecstasy","Educate","Efficient","Effective","Efficiency","Effortless"],
    'f': ["fable","faced","facer","faces","facet","facia","fabada","fabled","fabler","fables","fabric","facade"],
    'g': ["Gain","Giddy","Gaudy","Giant","Gate","Gaffe","Gale","Goofy","Gabby","Gamut","Godly","Goose"],
    'h': ["Happiness","Hair","Hardy","Handy","Heavy","Halcyon","Hadji","Hajji","Hamza","Hammy","Haggard","Hafiz"],
    'i': ["index","image","inlet","igloo","ideal","idiom","iambs","ichor","icily","idols","ilium","imply"],
    'j': ["Jackpot","Jack","Jaded","Jazzy","Jewel","Jaunt","Jab","Jabber","Jiffy","Jacky","Jammy","Jaggy"],
    'k': ["Key","Kennel","Kit","Knee","Keyboard","Knot","Knob","Kiwi","Fruit","Kettle","Kelp","Knife","Kitchen"],
    'l': ["Lean","Level","Lace","Late","Laudable","Lavish","Laconic phrase","Lucky","Lame","Lanky","Lute","Lackadaisical"],
    'm': ["Magnanimous","Majestic","Major","Magnificent","Magical","Mad","Mean","Master","Meet","Malleable","Macho","Mature"],
    'n': ["Neat","Nice","Naive","Naked","Narrow","Nascent","New","Niche","Natty","Nimble","Nirvana","Nonchalant"],
    'o': ["Oasis","Offer","Obtain","Oblique","Oakum","Onset","Oatmeal","Oblong","Obvious","Obsess","Older","Oomph"],
    'p': ["Patient","Prize","Pragmatics","Paramount","Patience","Prime","Pleasant","Persistent","Plentiful","Poetry","Palpable","Perky"],
    'q': ["Quiz","Quit","Quest","Queue","Quiet","Quite","Quote","Quint","Quill","Quail","Qualm","Quick"],
    'r': ["Rat","Rail","Rabbit","Rest","Ring","Rent","Rift","Rope","Rug","Rooster","Reverie","Rotation"],
    's': ["Self","Salt","Sky","Silk","Seed","Soap","Sauce","Stone","Shaft","Soul","Stunt","Stilt"],
    't': ["Tub","Tot","Tiger","Thief","Toss","Top","Thigh","Thud","Trough","Trash","Terrace","Thought"],
    'u': ["Unique","Unity","Ultimate","Unabashed","Unbiased","Unafraid","Unassuming","Unbelievable","Unconditional","Universal","Unconventional","Ubiquitous"],
    'v': ["Versatile","Vivacious","Vigilant","Venture","Vigorous","Visionary","Vapid","Voracious","Vacate","Valor","Vice","Vain"],
    'w': ["Wacky","Waffle","Waive","Waste","Wander","Waltz","White","Wager","Waiter","Waken","Weave","Waggish"],
    'x': ["Xylophone","Xerox","Xenophobia","Xebec","Xenial","Xanthic","Xystus","Xylene","Xanthous","Xanthate","Xenogamy","Xenolith"],
    'y': ["Yacht","Yawn","Yearn","Yell","Yeah","Yawp","Yoke","Yummy","Yawl","Yore","Yearly","Yogi"],
    'z': ["Zany","Zephyr","Zebra","Zappy","Zigzag","Zenith","Zesty","Zeal","Zarf","Zingy","Zilch","Zealous"]
}

def search_words(letter):
    return dictionary.get(letter.lower())

while True:
    user_input = input("Enter an alphabet to get its corresponding words ( or 'quit' to quit): ")
    
    if user_input == "quit":
        print("GoodBye___Thank You")
        break

    words = search_words(user_input)
    print("\n",str(words).replace('[',' ').replace(']',' ').replace("\'",' '),"\n")