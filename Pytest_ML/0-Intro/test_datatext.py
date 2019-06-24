import datatext as dtxt

import string
# This is here you writ the tests for a textual dataset

# Testing functions on textual data
"""
 Imagine we have textual data, and we want to clean it up. Therea are two functions we may want to write to standardize
 the data:

 -> bag_of_words(text), which takes in text and tokenizes the text into its set of constituent words
 -> strip_punctuation(test), which strips punctuations from the text

 design the tests first, abd then implement the two functions in datatext.py
"""

# Test if your text don't have punctuation
def test_strip_punctuation():
    text = 'random. stuff; typed, in-to th`is text^line'
    t = dtxt.strip_punctuation(text)                      # call function strip_punctuation to remove the puncts
    assert set(t).isdisjoint(string.punctuation)          # check if the punctuation was really removed

# Test if your text don't have punctuation
def test_bag_of_words():
    text = 'random stuff typed into this text line line'
    text_bagged = dtxt.bag_of_words(text)                  # call function bag_of_words to tokenize the text
    assert len(text_bagged) == 7                           # check the amount of unique words in the text
    assert ' ' not in text_bagged                          # check if we not have spaces identified as a word
