def is_one_word(text):
    return len(text.split) == 1

def start_end_same_char(text):
    return text[0] == text[-1]

def is_palindrome(text):
    if len(text) % 2 == 1:
        return False # uneven number of chars can't be a palindrom
    for char_pos in range(len(text) / 2):
        if text[char_pos] != text[0-(char_pos+1)]:
            return False
    return True
    # Create functions

# Create dispatch dictionary
func_dict = {"single" : is_one_word,
             "start_end" : start_end_same_char,
             "palindrome" : is_palindrome
            }
text = input("please provide a text: ")
user_input = input("""What is your command?
                     single = Is it one word True / False.
                     start_end = start/ends with the same char True/False.
                     palindrome = is it a palindrom True/False.
                     > 
                     """)

try:
    result = func_dict[user_input](text)
except KeyError as e:
    print("Command not available ", e)

print(result)