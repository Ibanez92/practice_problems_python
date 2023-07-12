country_file = open(r"countries/countries.txt", "r").read().split("\n")

# For loops and if conditions

# What are all of the countries that have “United” in the name?

def country_with_united(countries):
    for country in countries:
        if "United" in country:
            print(country)

country_with_united(country_file)

# What countries both begin and end with a vowel?

# What country names are > 50% vowels?

# Setting up storage to use during a for loop, including counters and arrays
# What is the shortest country name? Make sure your solution can handle ties.

# What countries use only one vowel in their name (the vowel can be used multiple times) - For example, if the word “BEEKEEPER” were a country, it would be an answer, because it only uses “E”.

# There is at least one country name that contains another country name. Find all of these cases.