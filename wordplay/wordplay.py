word_file = open(r"wordplay/sowpods.txt", "r").read().split('\n')
from collections import Counter

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

# def words_with_B_and_X_less_than_5letters(words):
#     for word in words:
#         if "b" in word.lower() and "x" in word.lower() and len(word) < 5:
#             print(word)

# words_with_B_and_X_less_than_5letters(word_file)

# What are all of the words that both start and end with a Y?

# def words_start_end_with_Y(words):
#     for word in words:
#         if word.lower().startswith('y') and word.lower().endswith('y'):
#             print(word)

# words_start_end_with_Y(word_file)

# What are all of the words with no vowel and not even a Y?

# def words_with_vowels_even_Y(words):
#     for word in words:
#         if "a" not in word.lower() and "e" not in word.lower() and "i" not in word.lower() and "o" not in word.lower() and "u" not in word.lower() and "y" not in word.lower():
#             print(word)

# words_with_vowels_even_Y(word_file)

# What are all of the words that have all 5 vowels, in any order?

# def words_with_all_5vowels(words):
#     for word in words:
#         if "a" in word.lower() and "e" in word.lower() and "i" in word.lower() and "o" in word.lower() and "u" in word.lower():
#             print(word)

# words_with_all_5vowels(word_file)

# What are all of the words that have all 5 vowels, in alphabetical order?

# arr_with_vowels = []

# def words_vowels_in_alphabetical_order(words):
#     for word in words:
#         if "a" in word.lower() and "e" in word.lower() and "i" in word.lower() and "o" in word.lower() and "u" in word.lower():
#             arr_with_vowels.append(word)

# words_vowels_in_alphabetical_order(word_file)

# sorted_list = sorted(arr_with_vowels)

# print(sorted_list)

# Setting up storage to use during a for loop, including counters and arrays

# How many words contain the substring "TYPE”?

# def count_words_TYPE(words):
#     count = 0
#     for word in words:
#         if "type" in word.lower():
#             count = count + 1
#     print(count)

# count_words_TYPE(word_file)

# Create and print an array containing all of the words that end in "GHTLY"

# arr_with_words_ending_in_GHTLY = []

# def words_end_in_GHTLY(words):
#     for word in words:
#         if word.lower().endswith("ghtly"):
#             arr_with_words_ending_in_GHTLY.append(word)

# words_end_in_GHTLY(word_file)

# print(arr_with_words_ending_in_GHTLY)

# What is the shortest word that contains all 5 vowels?

# list_of_vowels = []

# def shortest_word_with_all_5vowels(words):

#     for word in words:
#         if "a" in word.lower() and "e" in word.lower() and "i" in word.lower() and "o" in word.lower() and "u" in word.lower():
#             list_of_vowels.append(word)

#     smallest_len = len(min(list_of_vowels, key=len))
#     smallest = [name for name in list_of_vowels if len(name) == smallest_len]
#     print(smallest)

# shortest_word_with_all_5vowels(word_file)

# What is the longest word that contains no vowels?

# list_of_no_vowels = []

# def longest_word_with_all_5vowels(words):

#     for word in words:
#         if "a" not in word.lower() and "e" not in word.lower() and "i" not in word.lower() and "o" not in word.lower() and "u" not in word.lower():
#             list_of_no_vowels.append(word)

#     longest_len = len(max(list_of_no_vowels, key=len))
#     longest = [name for name in list_of_no_vowels if len(name) == longest_len]
#     print(longest)

# longest_word_with_all_5vowels(word_file)

# Which of the letters Q, X, and Z is the least common?

# dic = {
#     'Q':0,
#     'Z':0,
#     'X':0
# }

# def least_common_letters_Q_X_Z(words):
#     c = Counter()
#     for word in words:
#         for letter in word:
#             if letter in dic:
#                 c[letter] += 1
#     least_letter_with_count = c.most_common()[:-2:-1]
#     least_letter_in_dict = dict(least_letter_with_count)
#     for key in least_letter_in_dict.keys():
#         print("The least common letter is " + key)

# least_common_letters_Q_X_Z(word_file)

# What is the longest palindrome?

# What are all of the letters that never appear consecutively in an English word? For example, we know that “U” isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which letters never appear consecutively?