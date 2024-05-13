def main():
    path_to_file = "books/frankenstein.txt"
    contents = open_file(path_to_file)
    count_of_words = word_count(contents)
    count_of_characters = letter_count(contents)
    sorted_characters = sorted_character_count(count_of_characters)
    #print(contents)
    #print(count_of_words)
    #print(count_of_characters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_of_words} words were found in the document.")
    print()

    for item in sorted_characters:
        key = item['key']
        value = item['value']
        print(f"The '{key}' character was found {value} times.")
    
    print()
    print("--- End report ---")
    
def open_file(path_to_file):
    with open(path_to_file, 'r') as file:
        file_text = file.read()
    return file_text

def word_count(contents):
    word_list = contents.split()
    words = len(word_list)
    return words

def letter_count(contents):
    letter_dict = {}

    for char in contents:
        if char.isalpha():
            char = char.lower()
            letter_dict[char] = letter_dict.get(char, 0) +1

    return letter_dict

def sorted_character_count(count_of_characters):
    dictionary_list = []

    for key, value in count_of_characters.items():
        new_dict = {'key': key, 'value': value}
        dictionary_list.append(new_dict)

    def sort_on(item):
        return item['value']

    dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list

if __name__ == "__main__":

    main()
    """
    file_contents = main()
    count_of_words = word_count(file_contents)
    print(lower_contents)
    """


# Going to try to store global variables inside of the main() function and then call
# those values through to other functions, and finally call on main() in the if __name___
# section