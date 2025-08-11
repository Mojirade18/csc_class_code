# Caesar Cipher: shift letters by 3
letter = input("What are the words you want to cipher? ")
shift = 3
result = ""

for char in letter:
    if char.isalpha():  # only shift letters
        if char.isupper():
            ascii_offset = 65
        else:
            ascii_offset = 97
        new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        result += new_char
    else:
        result += char  # keep spaces, punctuation as is

print("Ciphered text:", result)
