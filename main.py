def main():
  book = "books/frankenstein.txt"
  text = get_book_text(book)
  num_words = get_num_words(text)
  print(f"{num_words}")

def get_num_words(text):
  words = text.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
main()