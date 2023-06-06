word_file = open(r"wordplay/sowpods.txt", "r").read().split('\n')

# What are all of the words containing UU?

# def words_with_UU(words):
#     for word in words:
#         if "uu" in word.lower():
#             print(word)

# words_with_UU(word_file)

# What are all of the words containing an X and a Y and a Z?

# def words_with_X_Y_Z(words):    
#     for word in words:
#         if "z" in word.lower() and "y" in word.lower() and "x" in word.lower():
#             print(word)

# words_with_X_Y_Z(word_file)

# What are all of the words containing a Q but not a U?
# def words_with_Q_not_U(words): 
#     for word in words:
#         if "q" in word.lower() and not "u" in word.lower():
#             print(word)

# words_with_Q_not_U(word_file)

# What are all of the words that contain the word CAT and are exactly 5 letters long?

# def words_with_CAT_5letters_long(words):
#     for word in words:
#         if len(word) == 5 and "cat" in word.lower():
#             print(word)

# words_with_CAT_5letters_long(word_file)

# What are all of the words that have no E or A and are at least 15 letters long?

# def words_with_E_or_A_15letters_long(words):
#     for word in words:
#         if "a" not in word.lower() and "e" not in word.lower() and len(word) == 15:
#             print(word)

# words_with_E_or_A_15letters_long(word_file)

# What are all of the words that have a B and an X and are less than 5 letters long?

def words_with_B_and_X_less_than_5letters(words):
    for word in words:
        if "b" in word.lower() and "x" in word.lower() and len(word) < 5:
            print(word)

words_with_B_and_X_less_than_5letters(word_file)

# What are all of the words that both start and end with a Y?

# What are all of the words with no vowel and not even a Y?

# What are all of the words that have all 5 vowels, in any order?

# What are all of the words that have all 5 vowels, in alphabetical order?

