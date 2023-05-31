def print_upper_words(words, must_start_with = {"h", "y"}):
    """ Iterate through the given list and print each out capitalized."""
    for word in words:
        result = word[0] in must_start_with 
        
        if result == True:
            print(word.upper())

