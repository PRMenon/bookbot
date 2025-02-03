def main():
    path = "books/frankenstein.txt"
    print_report(path)

def count_words(text):
    return len(text.split())

def count_characters(text:str):
    characters = {}
    
    for c in text.lower():
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    
    return characters

def sort_alphabets(d):
    char_list = []
    for c,count in d.items():
        if c.isalpha():
            char_list.append({"char": c, "count": count})
        
    char_list.sort(reverse = True, key = lambda item: item["count"] )
    return char_list

def print_report(path:str):
    with open(path) as f:
        file_contents = f.read()
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(file_contents)} words found in the document \n")
    
    chars = count_characters(file_contents)
    chars = sort_alphabets(chars)
    
    for item in chars:
        print(f"The character '{item["char"]}' appears {item["count"]} times")

    print("--- End Report ---")

main()

