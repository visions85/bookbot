def return_num_words(filepath):
    with open(filepath) as f:
        # Read in file contents
        file_contents = f.read()

        words = file_contents.split()

        wordcount = 0

        for word in words:
            wordcount += 1

    return wordcount

def count_chars(text):
    # Create an empty dictionary to store character counts
    char_counts = {}

    # Loop through each character in the text
    for char in text:
        # Convert the character to lowercase
        lowercase_char = char.lower()

        # If we've seen this character before, increment its count
        # If not, add it to the dictionary with a count of 1
        if lowercase_char in char_counts:
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1

    # Return the completed dictionary
    return char_counts

def sort_chars(char_counts):
    # Create empty list to hold our dictionary
    chars_list = []

    # Convert each character and count into a dictionary and add to the list
    for char, count in char_counts.items():
        chars_list.append({"char": char, "count": count})

    # Get the "count" value for sorting
    def sort_on(char_counts):
        return char_counts["count"]

    # Sort the list by count, descending
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
