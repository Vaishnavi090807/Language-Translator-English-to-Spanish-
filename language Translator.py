import tkinter as tk            # Importing tkinter library for GUI functionality


# Define dictionaries with translations
phrases = {
    "good morning": "buenos días",
    "good afternoon": "buenas tardes",
    "good evening": "buenas noches",
    "thank you": "gracias",
    "excuse me": "disculpa",   
    "where is...?": "¿dónde está...?",
    "how much is this?": "¿cuánto cuesta esto?",
    "i'm lost": "estoy perdido/a",
    "turn back": "vuelva atrás",
    "check-in": "entrada",
    "check-out": "salida",
    "how are you": "¿cómo estás?",
    "what's your name": "¿cómo te llamas?",
    "good night": "buenas noches",
    "exit": "salir",
    "please": "por favor",
}

dictionary = {
    "hello": "hola",
    "world": "mundo",
    "friend": "amigo",
    "goodbye": "adiós",
    "sorry": "lo siento",
    "yes": "sí",
    "no": "no",
    "maybe": "quizás",
    "left": "izquierda",
    "right": "derecha",
    "straight": "recto",
    "help": "ayuda",
    "police": "policía",
    "hospital": "hospital",
    "doctor": "médico",
    "emergency": "emergencia",
    "water": "agua",
    "food": "comida",
    "restaurant": "restaurante",
    "menu": "menú",
    "bill": "la cuenta",
    "hotel": "hotel",
    "room": "habitación",
    "reservation": "reserva",
    " ": " "
}

# Function to save translated text to a file
def save_translation(text, translation):
    with open("translations.txt", "a") as file:                          # Open file in append mode
        file.write(f"Original: {text}\nTranslation: {translation}\n\n")  # Write translation

# Function to translate text based on user's choice (word or phrase)
def translate_text():
    ask = translation_type.get()                                         # Get translation type (Word or Phrase) from user
    text = input_text.get()                                              # Get the text input from the user

    if ask == "W" or ask == "w":                                         # Check if translation is for a word
        text = text.lower()                                              # Convert input text to lowercase for consistency
        s = ""                                                           # Initialize an empty string for the result
        if text in dictionary:                                           # Check if word is in the dictionary
            translation = dictionary[text]
            output_text.set(translation)                                 # Set translation if found
            save_translation(text, translation)                          # Save translation to file
        elif " " in text:                                                # Handle multi-word entries
            lw = text.split()                                            # Split the text into words
            for i in lw:
                if i in dictionary:                                      # Translate each word if it exists
                    s = s + " " + dictionary[i]
            output_text.set(s.strip())                                   # Set the output text
            save_translation(text, s.strip())                            # Save translation to file
        else:
            output_text.set("Word not found in dictionary.")             # Message if word is not found
            
    elif ask == "P" or ask == "p":                                       # Check if translation is for a phrase
        text = text.lower()                                              # Convert input text to lowercase for consistency
        phrases_found = []                                               # List to hold found phrases
        for phrase in phrases:
            if phrase in text:                                           # Check if any phrase exists in the text
                phrases_found.append(phrase)                             # Add found phrases to the list
        
        if phrases_found:                                                # If any phrases were found
            result = ""
            for phrase in phrases_found:
                result += f"{phrase} -> {phrases[phrase]}\n"             # Format phrase and its translation
            output_text.set(result.strip())                              # Display all found phrases and their translations
            save_translation(text, result.strip())                       # Save translation to file
        else:
            output_text.set("Phrase not found.")                         # Message if phrase is not found
    else:
        output_text.set("[Unknown word or phrase]")                      # Message if the input is invalid

# Function to display dictionary content based on user choice
def show_dictionary():
    ask2 = dict_choice.get()                                             # Get dictionary choice (Word or Phrase) from user
    if ask2 == 1:                                                        # If Word Dictionary is selected
        result = "\n".join([f"{key}: {value}" for key, value in dictionary.items()])  # Format word dictionary
        output_text.set(result)                                          # Display word dictionary
    elif ask2 == 2:                                                      # If Phrase Dictionary is selected
        result = "\n".join([f"{key}: {value}" for key, value in phrases.items()])  # Format phrase dictionary
        output_text.set(result)                                                    # Display phrase dictionary
    else:
        output_text.set("Invalid choice for dictionary selection.")                # Message if input is invalid

# Function to display contents of translations.txt in the GUI
def view_saved_translations():
    try:
        with open("translations.txt", "r") as file:
            translations = file.read()
            output_text.set(translations)                                           # Display contents in output text area
    except FileNotFoundError:
        output_text.set("No translations saved yet.")                               # Message if file doesn't exist

# Create the main window
root = tk.Tk()                                                                      # Initialize the Tkinter root window
root.title("Language Translator (English-Spanish)")                                 # Set the window title

# Create title label
title_label = tk.Label(root, text="Language Translator", font=("Blackadder ITC", 72))
title_label.pack(pady=10)                                                           # Display title with padding

# Create radio buttons for translation type selection (Word or Phrase)
translation_type_label = tk.Label(root, text="Choose translation type (Word/Phrase):")
translation_type_label.pack()                                                       # Display label for translation type
translation_type = tk.StringVar(value="W")                                          # Variable to store user's choice (default to Word)
word_radio = tk.Radiobutton(root, text="Word", variable=translation_type, value="W")
phrase_radio = tk.Radiobutton(root, text="Phrase", variable=translation_type, value="P")
word_radio.pack()                                                                   # Display radio button for Word
phrase_radio.pack()                                                                 # Display radio button for Phrase

# Input text box for text to be translated
input_label = tk.Label(root, text="Enter text to translate:")
input_label.pack()                                                                 # Display label for text input
input_text = tk.Entry(root, width=50)                                              # Create entry field for text input
input_text.pack(pady=5)                                                            # Display entry field with padding

# Button to trigger translation
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=5)                                                      # Display translate button with padding

# Output display area for translation result
output_text = tk.StringVar()                                                       # Variable to store the output text
output_label = tk.Label(root, text="Translated text:")
output_label.pack()                                                                # Display label for output text
output_display = tk.Label(root, textvariable=output_text, width=100, height=15, relief="solid")
output_display.pack(pady=5)                                                        # Display output text area with padding

# Radio buttons to choose which dictionary to view (Word or Phrase)
dict_choice_label = tk.Label(root, text="View Dictionary (1 for Word, 2 for Phrase):")
dict_choice_label.pack()                                                            # Display label for dictionary choice
dict_choice = tk.IntVar(value=1)                                                    # Variable to store dictionary choice (default to Word)
dict_word_radio = tk.Radiobutton(root, text="Word Dictionary", variable=dict_choice, value=1)
dict_phrase_radio = tk.Radiobutton(root, text="Phrase Dictionary", variable=dict_choice, value=2)
dict_word_radio.pack()                                                             # Display radio button for Word Dictionary
dict_phrase_radio.pack()                                                           # Display radio button for Phrase Dictionary

# Button to show selected dictionary
view_dict_button = tk.Button(root, text="View Dictionary", command=show_dictionary)
view_dict_button.pack(pady=5)                                                     # Display button with padding

# Button to view saved translations
view_translations_button = tk.Button(root, text="View Saved Translations", command=view_saved_translations)
view_translations_button.pack(pady=5)                                              # Display view translations button with padding

# Start the GUI main loop
root.mainloop()                                                                    # Run the main loop to display the GUI
