alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzабвгґдеєзжиіїйклмнопрстуфхцшщьюяабвгґдеєзжиіїйклмнопрстуфхцшщьюя01234567890123456789"
encrypt = input("Enter a clear message: ")
key = 3
encrypt = encrypt.lower()
encrypted = ""
for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encrypted = encrypted + letter
print("Your cipher is: ", encrypted)
