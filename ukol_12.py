import os


def read_data(custom_idx=1,file_name="famous_quotes.txt"):
    """

    :param file_name: nazev filu
    :param custom_idx: pozice radku
    :return: list slov z radku
    """
    existuje = os.path.exists(file_name)

    if existuje == True:
        a_file = open(file_name)

        for position, line in enumerate(a_file):

            if position == custom_idx:
                listslov = line.replace(".","")
                listslov = listslov.replace(",","")
                listslov = listslov.replace("!","")
                listslov = listslov.replace("\n","")
                listslov = listslov.split(" ")
                for pozice,x in enumerate(listslov):
                    listslov[pozice] = x.lower()

        return listslov
    else:
        return None
def tokenize(listslov):
    """

    :param listslov: seznam slov
    :return: seznam tokenů

    """
    tokens = []
    for slovo in listslov:
        tokens.append(ord(slovo[0]))
    return tokens
def counting_sort(word_list):
    """

    :param word_list: vstupni list
    :return: slovnik  kumuolativni cetnost se stejnym znakem pocatecnim
    """

    word_list = word_list[::-1]
    output = {}

    tokens = tokenize(word_list)
    frequency = [0] * 256
    sorted_word_list = [0] * len(word_list)

    for token in tokens:
        frequency[token] += 1

    for symbol, count in enumerate(frequency):
        frequency[symbol] += frequency[symbol - 1]

    for i, element in enumerate(tokens):
        idx = frequency[element] - 1
        sorted_word_list[idx] = word_list[i]
        frequency[element] -= 1

    output["sorted_sequence"], output["frequency"] = sorted_word_list, frequency
    return output
def main():
    """

    :return: vse dohromady
    """
    # readdata

    word_list = read_data()
    print(word_list)

    # sort sequence
    sorted_sequence = counting_sort(word_list)
    print(sorted_sequence)


if __name__ == "__main__":
    main()
