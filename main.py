def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    generate_report(book, num_words, char_count)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
  
def get_char_count(text):
    dict = {}
    for char in text:
        lower = char.lower()
        if lower not in dict:
            dict[lower] = 1
        else:
            dict[lower] += 1
    return dict

def sort_on(dict):
    return dict["count"]

def get_sorted_list(char_count):
    temp_list = []
    for c in char_count:
        if c.isalpha():
            temp_list.append({"char": c, "count": char_count[c]})
    temp_list.sort(reverse=True, key=sort_on)
    return temp_list

def generate_report(book, num_words, char_count):
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document")
    print("")
    sorted = get_sorted_list(char_count)
    for item in sorted:
        print(f"The '{item["char"]}' character was found {item["count"]} times")
    print("--- End report ---")
main()