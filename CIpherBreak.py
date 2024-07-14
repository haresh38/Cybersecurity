#Haresh Shiwcharan
#Omoze Oyarebu
#Assignment 4: Break the Cipher using frequency Analysis
import matplotlib.pyplot as plt
from collections import Counter

#english frequencies
english_letter_frequency = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28,
    'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61,
    'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11,
    'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07
}
#known english bigrams
english_bilgram_frequency = {
    'th': 3.56, 'he': 3.02, 'in': 2.43, 'er': 2.05, 'an': 1.99,
    're': 1.86, 'nd': 1.81, 'at': 1.58, 'on': 1.48, 'nt': 1.41,
    'ha': 1.37, 'es': 1.34, 'st': 1.32, 'en': 1.29, 'ed': 1.27,
    'to': 1.26, 'it': 1.23, 'ou': 1.16, 'ea': 1.10, 'hi': 1.09,
    'is': 1.07, 'or': 1.06, 'ti': 1.05, 'as': 1.01, 'te': 0.98
}

#known english trigrams
english_trigrams_frequency = {
    'the': 1.82, 'and': 0.73, 'tha': 0.36, 'ent': 0.34, 'ing': 0.34,
    'ion': 0.32, 'tio': 0.31, 'for': 0.29, 'nde': 0.27, 'has': 0.26,
    'nce': 0.23, 'edt': 0.23, 'tis': 0.22, 'oft': 0.22, 'sth': 0.21,
    'men': 0.21
}

# Step 1: Prompt the user for Cipher Text
ciphertext = input("Enter the ciphertext: ").upper()
ciphertext2 = ciphertext.replace(" ", "")  # removes spaces

# Step 2: Frequency Analysis
# Function to calculate letter frequencies
def calculate_letter_frequency(text):
    frequency = Counter(text)
    return frequency

def calculate_bigram_frequency(text):
  # Bigrams Frequency in String 
  # Using a loop and dictionary 
  freq_dict = {}
  for i in range(1, len(text)):
      bigram = text[i-1:i+1]
      if bigram in freq_dict:
          freq_dict[bigram] += 1
      else:
          freq_dict[bigram] = 1
  
  return freq_dict

def print_bigrams(freq_dict):
    count = 0
    for bigram, freq in freq_dict.items():
        print(f"{bigram}: {freq}", end="   ")
        count += len(bigram) + len(str(freq)) + 3  # Calculate total length considering bigram, freq, and separators
        if count >= 45:
            print()  # Start a new line
            count = 0  # Reset count


def calculate_trigram_frequency(text):
    trigram_counts = {}
    text = text.upper()  # Convert text to uppercase to handle case insensitivity
    
    # Iterate through the text to count trigrams
    for i in range(len(text) - 2):
        trigram = text[i:i+3]
        if trigram in trigram_counts:
            trigram_counts[trigram] += 1
        else:
            trigram_counts[trigram] = 1
    
    return trigram_counts

def print_trigrams(trigrams):
    count = 0
    for trigram, freq in trigrams.items():
        print(f"{trigram}: {freq}", end="   ")
        count += len(trigram) + len(str(freq)) + 3  # Calculate total length considering trigram, freq, and separators
        if count >= 45:
            print()  # Start a new line
            count = 0  # Reset count

# Calculate frequencies
frequency1 = calculate_letter_frequency(ciphertext2)
frequency2 = calculate_bigram_frequency(ciphertext2)
frequency3 = calculate_trigram_frequency(ciphertext2)

#graphing
letters = sorted(frequency1.keys())
frequencies =[frequency1[letter] for letter in letters]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Cipher Text Frequency
ax1.bar(letters, frequencies, edgecolor='black')
ax1.set_xlabel('Letters')
ax1.set_ylabel('Frequency')
ax1.set_title('Cipher Text Frequency')

letters2 = list(english_letter_frequency.keys())
percentages = list(english_letter_frequency.values())

# Plot 2: English Letter Frequencies
ax2.bar(letters2, percentages)
ax2.set_xlabel('Letters')
ax2.set_ylabel('Frequency (%)')
ax2.set_title('English Letter Frequencies')
ax2.tick_params(axis='x', rotation=0)

# display the plots
plt.tight_layout()
plt.show()

#print bigram and trigram
print("Bigram English Frequency:\n")
print_bigrams(english_bigram_frequency)
print("\nBigram CipherText Frequency:\n")
print_bigrams(frequency2)
print("\n\nTrigram Ciphertext Freqency:\n")
print_trigrams(frequency3)
# Step 3: Mapping and decryption

# Function to create a mapping based on sorted frequencies
def create_mapping(ciphertext_frequency, english_frequency):
    # Get the 6 most common letters in the ciphertext
    sorted_ciphertext = sorted(ciphertext_frequency.items(), key=lambda x: x[1], reverse=True)
    top_ciphertext = [item[0] for item in sorted_ciphertext[:6]]

    # Get the 6 most common letters in English
    sorted_english = sorted(english_frequency.items(), key=lambda x: x[1], reverse=True)
    top_english = [item[0] for item in sorted_english[:6]]

    # Create the mapping
    mapping = {}
    for i in range(min(len(top_ciphertext), len(top_english))):
        mapping[top_ciphertext[i]] = top_english[i]

    return mapping


# Create mapping for 6 frequent only
mapping = create_mapping(frequency1, english_letter_frequency)
#print(mapping)

# Function to decrypt the ciphertext
def decrypt(ciphertext, mapping):
    deciphered_plaintext = ""

    print("\n\nOriginal Cipher Text:\n")
    print(ciphertext)

    for char in ciphertext:
        if char.upper() in mapping:
            if char.isupper():
                deciphered_plaintext += mapping[char.upper()].lower()
            else:
                deciphered_plaintext += char
        else:
            deciphered_plaintext += char  # If the character is not in mapping (spaces, special characters)

    print("\nInitial Deciphered Text:\n", deciphered_plaintext)

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
