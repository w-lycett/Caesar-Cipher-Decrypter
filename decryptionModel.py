# Import string for utilities to work with strings
import string

class CaesarModel:
    # Define constants for the alphabet and common letters (in order of frequency)
    ALPHABET = string.ascii_uppercase
    COMMON_LETTERS = "ETAOINSHRDLU"
    
    # Iterates through each character of the ciphertext, shifts it and adds it to the plaintext string
    def decrypt(self, ciphertext, shift):
        plaintext = ""
        for char in ciphertext:
            if char.upper() in self.ALPHABET:
                is_lower = char.islower()
                index = self.ALPHABET.index(char.upper())
                new_index = (index - shift) % 26
                new_char = self.ALPHABET[new_index]
                if is_lower:
                    new_char = new_char.lower()
                plaintext += new_char
            else:
                plaintext += char
        return plaintext

    # Scores the plaintext based on the frequency of common letters
    def score_text(self, plaintext):
        plaintext = plaintext.upper()
        score = 0
        for letter in self.COMMON_LETTERS:
            score += plaintext.count(letter)
        return score

    # Tries all possible shifts and returns the one with the highest score
    def crack_cipher(self, ciphertext):
        best_shift = None
        best_plaintext = ""
        best_score = -1
        for shift in range(26):
            plaintext = self.decrypt(ciphertext, shift)
            score = self.score_text(plaintext)
            if score > best_score:
                best_shift = shift
                best_plaintext = plaintext
                best_score = score
        return best_shift, best_plaintext