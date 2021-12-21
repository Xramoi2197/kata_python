def get_int(word: str) -> int:
    numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
    }
    if "-" in word:
        subwords = word.split("-")
        return numbers[subwords[0]] + numbers[subwords[1]]
    return numbers[word]


def parse_list_int(words: list) -> int:
    if len(words) == 1:
        return get_int(words[0])
    words.reverse()
    result = 0
    dozens = []
    find_patterns = ["one", "hundred", "thousand", "million", "max"]
    find_iterator = 1
    for word in words:
        if word in find_patterns and find_patterns.index(word) >= find_iterator :
            if len(dozens) != 0:
                result += parse_list_int(dozens) * get_int(find_patterns[find_iterator - 1])
                dozens = []
            find_iterator = find_patterns.index(word) + 1
        else:
            dozens.insert(0,word)
    if len(dozens) != 0:
        if find_iterator == 0:
            result += sum([get_int(subword) for subword in dozens])
        else:
            result += parse_list_int(dozens) * get_int(find_patterns[find_iterator - 1])
    else:
        result += get_int(find_patterns[find_iterator - 1])
    return result

def parse_int(string: str) -> int:
    words = string.split()
    words = list(filter(lambda x: x != "and", words))
    return parse_list_int(words)
    

if __name__ == "__main__":
    print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'))
    print(parse_int('two hundred forty-six'))
    print(parse_int('one'))
    print(parse_int('twenty'))
    print(parse_int('zero'))
    print(parse_int('one million two thousand and forty-six'))
    print(parse_int('one million'))
