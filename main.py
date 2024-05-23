def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    letter_counts = count_letters(text)

    letter_list = [{"letter": char, "num": count} for char, count in letter_counts.items()]

    letter_list.sort(reverse=True, key=sort_on)

    for item in letter_list:
         print(f"The '{item['letter']}' character was found {item['num']} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_letters(text):
    text = text.lower()
    letter_counts = {}
    for char in text: #loop througgh each character in text
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts

def sort_on(letter_counts):
    return letter_counts["num"]

main()

print("--- End Report ---")


