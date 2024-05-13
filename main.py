def main():

    path_to_file = "books/frankenstein.txt"

    with open(path_to_file, 'r') as file:
        contents = file.read()
        return contents

    
def word_count(contents):
    word_list = contents.split()

    count_of_words = len(word_list)

    return count_of_words

def letter_count(contents):
    lower_contents = contents.lower()
    return lower_contents

if __name__ == "__main__":
    file_contents = main()
    count_of_words = word_count(file_contents)
    print(lower_contents)