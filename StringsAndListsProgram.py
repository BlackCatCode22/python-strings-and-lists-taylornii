# StringsAndListsProgram.py

# Name: Taylor Nii
# Class: CIT-95
# Date: 9/3/2023

# PART 1: Strings
text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
print('text =', text)

# 1) Length Calculation: Write a function calculate_length(text)
def calculate_length(text):
    return len(text)
print('\nlength of text:', calculate_length(text))

# 2) Uppercase and Lowercase Conversion: Returns the text in uppercase letters followed by the text in lowercase letters
uppercase = text.upper()
print('\nUppercase:', uppercase)
lowercase = text.lower()
print('Lowercase:', lowercase)

# 3) Word Count: Write Python code that takes the given text as input and returns the total number of words in the text
word_count = text.strip().count(' ') + 1
print('word count:', word_count)

# 4) Substring Extraction: Returns the substring of text starting from the start index (inclusive) to end index (exclusive) supplied by a user.
start_index = int(input('Please give start index:\n'))
end_index = int(input('Please give end index (exclusive) ' + 'between ' + str(start_index + 1) + ' and ' + str(calculate_length(text)) + ':\n'))
substring = text[start_index:end_index]
print(substring)

# 5) Word Replacement: Takes a target word (input by the user) and replacement word (input by the user) as input,
#    returns the text with all occurrences of the target word replaced by the replacement word
target_word = input('Please input which word to replace:\n')
replacement_word = input('What would you like to replace "' + target_word + '" with?:\n')
word_replaced = text.replace(target_word, replacement_word)
print(word_replaced)

# 6) Whitespace Removal: Returns the text with all leading and trailing whitespaces removed
whitespaces_removed = text.strip()
print('\nleading/trailing spaces removed:', whitespaces_removed)

# 7) Splitting into Sentences: Write a function split_sentences(text) that takes the given text as input
#    returns a list of sentences present in the text.
def split_sentences(text):
    return text.split('.')
print(split_sentences(text))
# 8) Word Reversal: Returns the text with each word reversed
for i in range(len(text) - 1, -1, -1):
    print(text[i], end='')
print('')

# 9) Character Count: Takes a character as input & returns the number of occurrences of the specified character in the text
char = input('Please input a char:')
char_count = text.count(char)
print('Occurrences of "' + char + '" in text:', char_count)

# 10) Substring Count: Takes a substring as input & returns the number of occurrences of the specified substring in the text
substring = input('Please input a substring:')
substring_count = text.count(substring)
print('Occurrences of "' + substring + '" in text:', substring_count)

# PART 2: Lists
text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
print('\ntext =', text)

# 1) List Creation: Create a list called word_list by splitting the given text into words
word_list = text.replace(',', '')
word_list = word_list.replace('.', '').split()
print('\nword_list =', word_list)

# 2) Appending: Appending the word "Pythonic" to the word_list
word_list.append('Pythonic')
print('\nappended:', word_list)

# 3) Insertion: Insert the word "awesome" at the beginning of word_list
word_list.insert(0, 'awesome')
print('\ninsertion:', word_list)

# 4) indexing and Slicing: Print 3rd word in word_list & sublist 6-9th position
print('\n3rd word:', word_list[2])
print('6-9th word:', word_list[5:9])

# 5) Removal: Remove the word "amazing" from the word_list
word_list.remove('amazing')
print('\n"amazing" removed:', word_list)

# 6) Sorting: Sort the word_list in alphabetical order
word_list.sort()
print('\nalphabetical sort:', word_list)

# 7) Counting: Count the occurrences of the word "is" in the word_list
# Q: why does .count() not alter original word_list like .sort()?
print('\n"is" count:', word_list.count('is'))

# 8) Joining: Create a string sentence by joining the words in the word_list with spaces
sentence = ' '.join(word_list)
print('\njoined:', sentence)

# 9) Reversal: Reverse the order of elements in word_list
word_list.reverse()
print('\nreversed:', word_list)

# 10) Copying: Create a new list copied_list by copying the contents of word_list
copied_list = word_list.copy()
print('\nnew_list =', copied_list)
