def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number = number_of_words(text)
    letters = number_of_letters(text)
    lista = dic_to_lst(letters)
    print("\n-----Begin report of books/frankenstein.txt--- \n")
    print(f"{number} words were found in the document\n")
    for i in lista:
        if not i["char"].isalpha():
            continue
        print(f"{i["char"]} character was found {i["num"]} times")
    print("\n ------------- End report -------------")
   # print(f"\n {number} words are found in the document \n")
   # for i in letters:
    #    print(f"The {i} character was found {letters[i]} times")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(d):
    return d["num"]

def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_letters(text):
    slova = {}
    for i in text:
        mala = i.lower()
        if mala in slova:
            slova[mala] += 1
        else:
            slova[mala] = 1
    return slova

def dic_to_lst(dic):
    lista = []
    for i in dic:
        lista.append({"char": i, "num": dic[i]})
    lista.sort(reverse=True, key=sort_on)
    return lista

main()