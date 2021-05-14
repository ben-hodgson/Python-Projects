from guizero import App, Text, TextBox, PushButton

app = App(title='HelloWorld!!')

hello_text = Text(app, text='HelloWorld!!', font='Helvetica', size=60)


whatever = TextBox(app, width=50, multiline=True, height=5)
whatever.value='Something Cool'

button = PushButton(app, text='Push Me!!')
button.width=6
button.height=3

app.display()