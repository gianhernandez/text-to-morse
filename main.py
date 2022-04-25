dictionary = {}

# Opens file with Alphabet value to morse code
with open('morse.txt') as file:
    for line in file:
        (key, value) = line.split()
        dictionary[key] = value

user_text = input('Enter phrase to convert to morse code: ').upper()
print(user_text)

morse_code = ''
for letter in user_text:
    if letter in dictionary.keys():
        print(dictionary[letter])
        morse_code += dictionary[letter]



