#########################################
##            imports                  ##
#########################################
from guizero import App, Text, PushButton, TextBox
from tkinter import *


#########################################
##             functions               ##
#########################################
aplhabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''
def outMessage():
    print("button was pressed!!!!!")
    for character in inMessage:
        if character in aplhabet:
            position = aplhabet.find(character)
            newPosition = (position + key) % 26
            newCharacter = aplhabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character

#########################################
##               app                   ##
#########################################
app = App("Encryption")

#########################################
##              widgets                ##
#########################################
inMessage = TextBox(app, width=50, multiline=True, height=5, text="Enter your Message:")
button = PushButton(app, outMessage, text="Encrypt your message.")


#########################################
##              display                ##
#########################################
app.display()