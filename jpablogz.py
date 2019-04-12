# Ej: python jpablogz.py GCG


# We need the sys Python Library
import sys


# try assign in to the variable the parameter to the python file
try:
  PATTERN = sys.argv[1]
except:
  print('The pattern is required')
  sys.exit()


# The dataset variable is the dataset file opened
dataset = open("dataset_2_71.txt", "r")


# This function return the count of the patterns in the file content
def pattern_count(pattern=None, text=None):

  # If the text or file content is None the program will be finished
  if text == None or pattern == None:
    print('Text and Data set file is requiered')
    sys.exit()

  # We need initialize count as 0
  count = 0

  # For letter in "text length"
  for letter_count in range(len(text)-len(pattern) +1 ):

    # If the current letter count is equal to the current letter_count + the length of the pattern
    # Ej string[0: 0 + 3] is "GCG"
    if text[letter_count: letter_count + len(pattern)] == pattern:
      count += 1

  # We print the count
  print(count)


# We need call the function to run it
pattern_count(pattern=PATTERN, text=dataset.read())



