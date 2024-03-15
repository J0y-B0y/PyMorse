#+----------------------+
#|   Module Section     |
#+----------------------+

# Imports the necessary libraries: speech_recognition for audio recognition and colorama for colored text output.

import speech_recognition as sr, colorama

# Defines a dictionary "morsedb" that maps characters to their Morse code representations.
morsedb = {
    " ":" / ",

    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",

    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",

    ".":".-.-.-",
    ",":"--..--",
    "?":"..--..",
    "!":"-.-.--",
    "'":".----.",
    '"':".-..-.",
    "(":"-.--.",
    ")":"-.--.-",
    "/":"-..-.",
    ":":"---...",
    "+":".-.-.",
    "=":"-...-",
    "&":".-...",
    "_":"..--.-",
    "-":"-....-",
}

#+-----------------------------------------+
#|       Program Functions Section         |
#+-----------------------------------------+

# Defines a function "Text2Morse" that takes a text input and converts it to Morse code using the provided Morse dictionary.

def Text2Morse(InputText: str, MorseDict = morsedb):
    # Converts the input text to lowercase.
    InputText = InputText.lower()
    # Initializes variables for storing Morse code output.
    morseout = ""
    currentmorse = ""
    # Iterates over each character in the input text.
    for element in InputText:
        # Finds the Morse code representation for the current character.
        for key, value in MorseDict.items():
            if key == element:
                currentmorse = value
        # Appends the Morse code representation of the current character to the output string.
        morseout+=currentmorse+" "
    # Returns the Morse code output string, removing the trailing space.
    return morseout[:-1]

# Defines a function AudioInput for capturing audio input.

def AudioInput():
    # Initializes a speech recognizer object.
    recognizer = sr.Recognizer()

    # Opens the microphone as a source for audio input.
    with sr.Microphone() as source:
        # Prints a message and adjusts for ambient noise before capturing audio.
        print(colorama.Fore.RED + "Receiving Audio...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    # Tries to recognize the audio input using Google's speech recognition service and returns the recognized text.
    try:
        print(colorama.Fore.YELLOW + "Processing Audio...")
        user_input = recognizer.recognize_google(audio)
        return user_input
    
    # Handles the case where audio input cannot be recognized.
    except sr.UnknownValueError:
        print(colorama.Fore.RED + "Issues Interpreting Audio")
        return None

#+-----------------------------------------+
#|      Main Program Execution Section     |
#+-----------------------------------------+

# Asks the user to select the input mode.

AudioQ = str(input(colorama.Fore.BLUE + "0: Audio-Morse Mode; 1: Text-Morse Mode: ")) 

# If the user chooses audio input mode; Calls the AudioInput function to get audio input, then prints the decoded text and its Morse code representation.
if AudioQ == "0":
    input_text = AudioInput()
    if input_text:
        print(colorama.Fore.YELLOW + "\nDecoded:", input_text)
        print(colorama.Fore.GREEN + "Encoded:", Text2Morse(input_text))

# If the user chooses text input mode; Prompts the user for text input, then prints the Morse code representation of the input text.
elif AudioQ == "1":
    TextIn = str(input(colorama.Fore.YELLOW + "Requesting Text Input: "))
    print(colorama.Fore.GREEN + "Decoded:", Text2Morse(TextIn))

# Handles the case where the user provides an invalid input mode.
else:
    print(colorama.Fore.RED + "Invalid Input Medium Selection")
