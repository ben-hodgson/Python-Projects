alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3 # amount to move to the right
newMessage = ''

#print("Letter 1 = ", alphabet[0], "This is position 0")
#print("Letter 7 = ", alphabet[6], "This is position 6")
#print("Letter 19 = ", alphabet[18], "This is position 18")
#print("Letter 26 = ", alphabet[25], "This is position 25")

#character = input('Please enter a character: ')
message = input('Please enter a message: ')

for character in message:
    if character in alphabet:
        position = alphabet.find(character)  # Find letter position in alphabet
        newPosition = (position + key) % 26  # add amount in key to alphabet position loop back to a when going past z
        newCharacter = alphabet[newPosition]  # select the new character that is the value of the key away from the original
        newMessage += newCharacter  # add new characters together for a new string
    else:
        newMessage += character  # only convert letters not spaces or special characters
    #print("That is letter ", position + 1)  
    #print("The new letter is in position", newPosition, "and is letter", position + 1)   
    #print("When adding 3 onto", character, "it becomes", newCharacter)
    #print("The new character is: ", newCharacter)
    #print(newMessage)

print("The new message is: ", newMessage)  # output converted message.
