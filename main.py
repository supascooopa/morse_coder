import string
# ---- morse code dictionary ---- #
morse_dict = {"a": ".-",
              "b": "-...",
              "c": "-.-.",
              "d": "-..",
              "e": ".",
              "f": "..-.",
              "g": "--.",
              "h": "....",
              "i": "..",
              "j": ".--",
              "k": "-.-",
              "l": ".-..",
              "m": "--",
              "n": "-.",
              "o": "---",
              "p": ".--.",
              "q": "--.-",
              "r": ".-.",
              "s": "...",
              "t": "-",
              "u": "..-",
              "v": "...-",
              "w": ".--",
              "x": "-..-",
              "y": "-.--",
              "z": "--.."}


def reading_file(file_path=""):
    with open(file_path) as file:
        lines = file.readlines()
    joined_lines = " ".join(lines)
    return joined_lines


def convert_to_morse(word="", file_path=""):
    """ Converts text to morse code
    word: A string that the user provides
    file_path: User can provide a text file to be converted to morse code"""
    punctuation = string.punctuation  # a list of punctuations in order to filter them out
    escape_character = ["\n", "\t"]  # a list of escape characters most commonly found in strings to filter out
    morse_code = ""
    # if file path is present replace the word parameter with it
    if file_path:
        word = reading_file(file_path)
    for letter in word:
        # a space means end of a word therefore there should be a special indicator for it, so I added the word 'STOP'
        # with spaces in the beginning and the end in order to not mix with rest of the code
        if letter == " ":
            morse_code = morse_code + " STOP "
        # filtering out punctuations and escape characters
        elif letter not in punctuation and letter not in escape_character:
            morse_code = morse_code + morse_dict[letter.lower()] + " "
    return morse_code


def convert_morse_to_text(code=""):
    """ converts morse code into words.
     code: A string of morse code made up of dots '.' and dashes '-' and the word 'STOP'
     All letters represented in morse code are divided by space and every word ending is identified by 'STOP'.
     """
    sentence = ""
    split_code = code.split(" ")  # splits all the strings with space
    # reversing the morse code in order to decipher it.
    reversed_morse_dict = {morse: letter for letter, morse in morse_dict.items()}
    for c in split_code:
        # Adding space to all instances of the word "STOP"
        if c == "STOP":
            sentence = sentence + " "
        elif c != " " and c:
            sentence = sentence + reversed_morse_dict[c]
    return sentence



