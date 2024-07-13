#Haresh Shiwcharan
#Omoze Oyarebu
#Assignment 4: Break the Cipher using frequency Analysis

import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Prompt the user for Cipher Text
ciphertext = input("Enter the ciphertext: ").upper()
ciphertext2 = ciphertext.replace(" ", "")  # removes spaces

# Step 2: Frequency Analysis
# Convert the ciphertext to a list of characters
letters = list(ciphertext2)

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

# Create a mapping based on sorted frequencies
sorted_ciphertext_frequency = [item[0] for item in frequency.most_common()]
sorted_english_frequency = sorted(english_letter_frequency.keys(), key=lambda x: english_letter_frequency[x], reverse=True)

# maps the ciphertext most frequent letters with the standard english letters most frequent letters(one-to-one)
mapping = dict(zip(sorted_ciphertext_frequency, sorted_english_frequency))
#print("\nMapped:\n", mapping)

# Function to decrypt the ciphertext
def decrypt(ciphertext, mapping):
    deciphered_plaintext = ""

    print("\n\nOriginal Cipher Text:\n")
    print(ciphertext)

    for char in ciphertext:
        if char in mapping:
            deciphered_plaintext += mapping[char]
        else:
            deciphered_plaintext += char  # If the character is not in mapping(spaces)

    print("\nDeciphered Text:\n", deciphered_plaintext)

    # Ask user if they want to modify the decrypted text
    modify_text = input("\nWould you like to modify the deciphered text? (y/n): ").lower()
    if modify_text == 'y':
        while True:
            find_char = input("Enter the character you wish to replace (or 'exit' to finish): ")
            if find_char == 'exit':
                break
            replace_char = input("Replace with: ")
            deciphered_plaintext = deciphered_plaintext.replace(find_char, replace_char)

            print("\nModified Deciphered Text:\n", deciphered_plaintext)

# Call the decryption function
decrypt(ciphertext, mapping)
