#Haresh Shiwcharan
#Omoze Oyarebu
#Assignment 4: Break the Cipher using frequency Analysis

import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Prompt the user for Cipher Text
ciphertext = input("Enter the ciphertext: ").upper()

# Step 2: Frequency Analysis
# Convert the ciphertext to a list of characters
letters = list(ciphertext)

# Count the frequency of each letter
frequency = Counter(letters)

# Prepare data for plotting
letters = sorted(frequency.keys())
frequencies = [frequency[letter] for letter in letters]

# Frequency graph
plt.bar(letters, frequencies, edgecolor='black')
plt.xlabel('Letters')
plt.ylabel('Frequency')
plt.title('Cipher Text Frequency')
plt.show()



#step 3
#source:https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
english_letter_frequency = {
    'E': 12.02,
    'T': 9.10,
    'A': 8.12,
    'O': 7.68,
    'I': 7.31,
    'N': 6.95,
    'S': 6.28,
    'R': 6.02,
    'H': 5.92,
    'D': 4.32,
    'L': 3.98,
    'U': 2.88,
    'C': 2.71,
    'M': 2.61,
    'F': 2.30,
    'Y': 2.11,
    'W': 2.09,
    'G': 2.03,
    'P': 1.82,
    'B': 1.49,
    'V': 1.11,
    'K': 0.69,
    'X': 0.17,
    'Q': 0.11,
    'J': 0.10,
    'Z': 0.07
}



# Initialize an empty string for the deciphered text
deciphered_text = ""
