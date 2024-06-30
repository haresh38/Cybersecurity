#Haresh Shiwcharan
#Omoze Oyarebu
#Assignment 4: Break the Cipher using frequency Analysis

from collections import Counter

# First I want to prompt the user for Cipher Text
ciphertext = input("Enter the ciphertext: ").upper()

# Step 2: Frequency Analysis
# Convert the ciphertext to a list of characters
letters = list(ciphertext)

# Count the frequency of each letter
frequency = Counter(letters)

# Initialize an empty string for the deciphered text
deciphered_text = ""
