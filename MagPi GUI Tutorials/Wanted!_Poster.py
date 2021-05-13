from guizero import App, Text, Picture
# Title of app window
app = App("Wanted!")
app.bg = "#b29a52"  # background colour / it cab be named, hex or RGB
wanted_Text = Text(app, text="WANTED")
wanted_Text.text_size = 50
wanted_Text.font = "Times New Roman"
Alex = Picture(app, image="images/Alex_418.png")

# app.display() must be present for the window to show
app.display()
