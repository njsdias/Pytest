
# Here you write the pre-processing text functions

import string

# eliminate the punctuation
def strip_punctuation(text):
    exclude = string.punctuation
    return ''.join(s for s in text if s not in exclude)

# t = "hello world! This is my pleasure, and the 2nd time I've been to PyCon!"

# tokenize the text
def bag_of_words(text):
    text = strip_punctuation(text)
    words = set(text.split(' '))
    return words