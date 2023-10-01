"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Šplíchal
email: p.splichal98@gmail.com
discord: Petr Š
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

sep = "-" * 40
texts_count = len(TEXTS)
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

# přihlášení a ověření uživatele
username = input("username: ")
password = input("password: ")
print(sep)

if registered_users.get(username) != password:
    print("Unregistered user, terminating the program.")
    quit()    

print(f"Welcome to the app, {username}")
print(f"We have {texts_count} texts to be analyzed. \n{sep}")

# výběr textu
choice = input(f"Enter a number btw. 1 and {texts_count} to select: ")

if not choice.isnumeric():
    print("Wrong format.")
    quit()
choice = int(choice)

if choice < 1 or choice > texts_count:
    print("Wrong number.")
    quit()

print(sep)

# rozdělení textu
clean_words = []
for word in TEXTS[choice - 1].split():
    clean_word = word.strip(".,:;!?_@")
    clean_words.append(clean_word)

# textová analýza
word_count = len(clean_words)
title_count = 0
upper_count = 0
lower_count = 0
num_count = 0
num_sum = 0
for word in clean_words:
    if word.istitle():
        title_count = title_count + 1
    elif word.isupper() and word.isalpha():
        upper_count += 1
    elif word.islower() and word.isalpha():
        lower_count += 1
    elif word.isnumeric():
        num_count += 1
        num_sum += int(word)

# vypsání výsledků analýzy
print(f"There are {word_count} words in the selected text. \n\
There are {title_count} titlecase words. \n\
There are {upper_count} uppercase words. \n\
There are {lower_count} lowercase words. \n\
There are {num_count} numeric strings. \n\
The sum of all the numbers {num_sum}. \n{sep}"
) 

# rozdělení slov
word_lenghts = {}
for word in clean_words:
    word = word.strip(".,:;!?_@")
    lenght = len(word)
    if lenght not in word_lenghts:
        word_lenghts[lenght] = 1
    else:
        word_lenghts[lenght] += 1

# korekce sudého odsazení v grafu
max_word = max(word_lenghts.values())
if not max_word % 2:
    max_word += 1

print(f"LEN|{' ' * int(max_word / 2)}OCCURENCES{' ' * int(max_word / 2)}|NR. \
      \n {sep}")

# vypsání grafu
for lenght, count in sorted(word_lenghts.items()):
    if lenght <= 9:
        print("", lenght,"|", '*' * count, " " * (max_word - count + 6), "|",count)
    else:
        print(lenght,"|", '*' * count, " " * (max_word - count + 6), "|",count)
