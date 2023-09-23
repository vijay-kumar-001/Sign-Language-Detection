import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
my_string = ""
labels = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
          "X", "Y")
# Convert the string to a list of characters
string_list = ""
element1 = "s"
element2 = "k"
element3 = "y"
my_string += labels[17]
my_string += labels[9]
my_string += labels[23]
# Define the text you want to convert to speech
text = "hiam"
# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 10.0)  # Volume (from 0.0 to 1.0)

# Convert and speak the text
engine.say(my_string)

# Block while processing all the currently queued commands
engine.runAndWait()