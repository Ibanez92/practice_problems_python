word_file = open(r"wordplay/sowpods.txt", "r").read().split('\n')

# What are all of the words containing UU?
# for word in word_file:
#     if "UU" in word:
#         print(word)

# What are all of the words containing an X and a Y and a Z?
def words_with_x_y_z(words):    
    for word in word_file:
        if "x" "y" "z" in word.lower():
            print(word)

words_with_x_y_z(word_file)

# What are all of the words containing a Q but not a U?
# def words_with_q_not_u(words): 
#     for word in word_file:
#         if "Q" in word and not "U" in word:
#             print(word)

# words_with_q_not_u(word_file)

# What are all of the words that contain the word CAT and are exactly 5 letters long?

# What are all of the words that have no E or A and are at least 15 letters long?

# What are all of the words that have a B and an X and are less than 5 letters long?

# What are all of the words that both start and end with a Y?

# What are all of the words with no vowel and not even a Y?

# What are all of the words that have all 5 vowels, in any order?

# What are all of the words that have all 5 vowels, in alphabetical order?

